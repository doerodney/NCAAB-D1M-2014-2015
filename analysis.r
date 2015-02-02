setwd("c:/github/doerodney/NCAAB-D1M-2014-2015")

df = read.csv("dataframe.csv", header=TRUE)

summary(df)

# margin of victory
# df$mov = df$win_points_scored - df$loss_points_scored

pythagorean_expectation <- function(scored, allowed, n) {
	py_ex = scored^n / (scored^n + allowed^n)
	return(py_ex)
}

pythagorean_expectation_root<-function(x, points_scored, points_allowed, win_fraction) {
	result = points_scored^x / (points_scored^x + points_allowed^x) - win_fraction
	return(result)
}

get_pythogorean_expectation_exponent<-function(points_scored, points_allowed, win_fraction) {
	n = uniroot(pythagorean_expectation_root, c(0.1, 
	100.0), points_scored = 1000, points_allowed = 800, win_fraction = 0.8)
	return(n)
}

# remove low contributors
plotFit <- function(yObserved, yFitted, intercept=0) {
  plot(yObserved, yFitted, xlab="Actual", ylab="Predicted")
  abline(intercept, 1, lty=2, col=rgb(1,0,0))
}

model = lm(win_points_scored ~
	win_conference + 
	win_possessions + 
	win_offensive_rating + 
	win_defensive_rating + 
	win_personal_fouls + 
	loss_conference + 
	loss_possessions + 
	loss_offensive_rating + 
	loss_defensive_rating + 
	loss_defensive_rebounds + 
	loss_steals + 
	loss_blocked_shots + 
	loss_personal_fouls,
	data=df)

plotFit(df$win_points_scored, fitted(model))

getPossessions <- function(df, teamName) {
    df <- as.data.frame(df)
    Possessions <- c(df$win_possessions[which(df$win_team == teamName)],
                     df$loss_possessions[which(df$loss_team == teamName)])
    return(Possessions)
}


getOffensiveRatings <- function(df, teamName) {
    df <- as.data.frame(df)
    OffensiveRatings <- c(df$win_offensive_rating[which(df$win_team == teamName)],
                          df$loss_offensive_rating[which(df$loss_team == teamName)])
    return(OffensiveRatings)
}


getDefensiveRatings <- function(df, teamName) {
    df <- as.data.frame(df)
    DefensiveRatings <- c(df$win_defensive_rating[which(df$win_team == teamName)],
                          df$loss_defensive_rating[which(df$loss_team == teamName)])
    return(DefensiveRatings)
}


getDefensiveRebounds <- function(df, teamName) {
    df <- as.data.frame(df)
    DefensiveRebounds <- c(df$win_defensive_rebounds[which(df$win_team == teamName)],
                              df$loss_defensive_rebounds[which(df$loss_team == teamName)])
    return(DefensiveRebounds)
}


getPersonalFouls <- function(df, teamName) {
    df <- as.data.frame(df)
    PersonalFouls <- c(df$win_personal_fouls[which(df$win_team == teamName)],
                       df$loss_personal_fouls[which(df$loss_team == teamName)])
    return(PersonalFouls)
}


getSteals <- function(df, teamName) {
    df <- as.data.frame(df)
    Steals <- c(df$win_steals[which(df$win_team == teamName)],
                df$loss_steals[which(df$loss_team == teamName)])
    return(Steals)
}


getBlockedShots <- function(df, teamName) {
    df <- as.data.frame(df)
    BlockedShots <- c(df$win_blocked_shots[which(df$win_team == teamName)],
                      df$loss_blocked_shots[which(df$loss_team == teamName)])
    return(BlockedShots)
}


getTeamConference <- function(df, teamName) {
    df <- as.data.frame(df)
  
    TeamConferences = df$win_conference[which(df$win_team == teamName)]
    if (length(TeamConferences) == 0) {
        TeamConferences = df$loss_conference[which(df$loss_team == teamName)]
    }
    return(as.character(TeamConferences[1]))
}

predictWinner <- function(teamName, opponentName, df, model, nScenarios=10000)
{
    teamConference = getTeamConference(df, teamName)
    teamPossessions = getPossessions(df, teamName)
    teamOffensiveRatings = getOffensiveRatings(df, teamName)
    teamDefensiveRatings = getDefensiveRatings(df, teamName)
    teamDefensiveRebounds  = getDefensiveRebounds(df, teamName)
    teamSteals = getSteals(df, teamName)
    teamPersonalFouls = getPersonalFouls(df, teamName)
    teamBlockedShots = getBlockedShots(df, teamName)

    opponentConference = getTeamConference(df, opponentName)
    opponentPossessions = getPossessions(df, opponentName)
    opponentOffensiveRatings = getOffensiveRatings(df, opponentName)
    opponentDefensiveRatings = getDefensiveRatings(df, opponentName)
    opponentDefensiveRebounds  = getDefensiveRebounds(df, opponentName)
    opponentSteals = getSteals(df, opponentName)
    opponentPersonalFouls = getPersonalFouls(df, opponentName)
    opponentBlockedShots = getBlockedShots(df, opponentName)

    win_conference = rep(teamConference, nScenarios)
    win_possessions = sample(min(teamPossessions):max(teamPossessions), nScenarios, replace=TRUE)
    win_offensive_rating = runif(nScenarios, min(teamOffensiveRatings ), max( teamOffensiveRatings ))
    win_defensive_rating = runif(nScenarios, min(teamDefensiveRatings), max(teamDefensiveRatings))
    win_personal_fouls = sample(min(teamPersonalFouls):max(teamPersonalFouls), nScenarios, replace=TRUE)
    loss_conference = rep(opponentConference, nScenarios)
    loss_possessions = sample(min(opponentPossessions):max(opponentPossessions), nScenarios, replace=TRUE)
    loss_offensive_rating = runif(nScenarios, min(opponentOffensiveRatings), max(opponentOffensiveRatings))
    loss_defensive_rating = runif(nScenarios, min(opponentDefensiveRatings), max(opponentDefensiveRatings))
    loss_defensive_rebounds = runif(nScenarios, min(opponentDefensiveRebounds), max(opponentDefensiveRebounds))
    loss_steals = sample(min(opponentSteals):max(opponentSteals), nScenarios, replace=TRUE)
    loss_blocked_shots = sample(min(opponentBlockedShots):max(opponentBlockedShots), nScenarios, replace=TRUE)
    loss_personal_fouls = sample(min(opponentPersonalFouls):max(opponentPersonalFouls), nScenarios, replace=TRUE)

    # Create data frame for team score prediction.
    dfpt = cbind.data.frame(
        win_conference,
        win_possessions,
        win_offensive_rating,
        win_defensive_rating,
        win_personal_fouls,
        loss_conference,
        loss_possessions,
        loss_offensive_rating,
        loss_defensive_rating,
        loss_defensive_rebounds,
        loss_steals,
        loss_blocked_shots,
        loss_personal_fouls
    )

    teamPointsScored = round(predict(model, dfpt))

    # Create data frame for opponent score prediction.
    # Switch conferences
    x = loss_conference
    loss_conference = win_conference
    win_conference = x

    # Switch possessions
    x = loss_possessions
    loss_possessions = win_possessions
    win_possessions = x

    # Switch offensive ratings
    x = loss_offensive_rating
    loss_offensive_rating = win_offensive_rating
    win_offensive_rating = x

    # Switch defensive ratings
    x = loss_defensive_rating
    loss_defensive_rating = win_defensive_rating
    win_defensive_rating= x

    win_personal_fouls = sample(min(opponentPersonalFouls):max(opponentPersonalFouls), nScenarios, replace=TRUE)

    loss_defensive_rebounds = runif(nScenarios, min(teamDefensiveRebounds), max(teamDefensiveRebounds))
    loss_steals = sample(min(teamSteals):max(teamSteals), nScenarios, replace=TRUE)
    loss_blocked_shots = sample(min(teamBlockedShots):max(teamBlockedShots), nScenarios, replace=TRUE)
    loss_personal_fouls = sample(min(teamPersonalFouls):max(teamPersonalFouls), nScenarios, replace=TRUE)

    dfpo = cbind.data.frame(
        win_conference,
        win_possessions,
        win_offensive_rating,
        win_defensive_rating,
        win_personal_fouls,
        loss_conference,
        loss_possessions,
        loss_offensive_rating,
        loss_defensive_rating,
        loss_defensive_rebounds,
        loss_steals,
        loss_blocked_shots,
        loss_personal_fouls
    )

    # Predict opponent points scored.
    opponentPointsScored = round(predict(model, dfpo))

    # Make a dataframe of points scored.  Not sure why...
    pointsScored = cbind.data.frame(teamPointsScored, opponentPointsScored)

    # Produce/report a result message.
    teamWins = pointsScored$teamPointsScored > pointsScored$opponentPointsScored
    msg = sprintf("%d scenarios of %s versus %s:", nScenarios, teamName, opponentName)
    print(msg)
    nTeamWins = length(which(teamWins == TRUE))
    nOpponentWins = nScenarios - nTeamWins
	margin = numeric(nScenarios)
	xlabel = ''
	ylabel = 'Simulated margin of victory'
	x = seq(1:nScenarios)
    if (nTeamWins > nOpponentWins) {
		margin = sort(pointsScored$teamPointsScored - pointsScored$opponentPointsScored)
		xlabel = sprintf("%s wins %d scenarios with a mean margin of %4.1f.", teamName, nTeamWins, mean(margin))
    } else {
		margin = sort(pointsScored$opponentPointsScored - pointsScored$teamPointsScored)
		xlabel = sprintf("%s wins %d scenarios with a mean margin of %4.1f.", opponentName, nOpponentWins, mean(margin))
    }
	plot(x, margin, main=msg, xlab=xlabel, ylab=ylabel, pch=6)
	abline(h=0)
	abline(v=(nScenarios/2))
    print(xlabel)
	
	#return(pointsScored)
}
#predictWinner('villanova-wildcats', 'seton-hall-pirates', df, model)
#predictWinner('villanova-wildcats', 'st-johns-red-storm', df, model)
#predictWinner('villanova-wildcats', 'depaul-blue-demons', df, model)
#predictWinner('villanova-wildcats', 'xavier-musketeers', df, model)
#predictWinner('villanova-wildcats', 'penn-quakers', df, model)
#predictWinner('villanova-wildcats', 'georgetown-hoyas', df, model)
#predictWinner('villanova-wildcats', 'creighton-bluejays', df, model)
#predictWinner('villanova-wildcats', 'depaul-blue-demons', df, model)
#predictWinner('villanova-wildcats', 'marquette-golden-eagles', df, model)
#predictWinner('villanova-wildcats', 'georgetown-hoyas', df, model)
#predictWinner('villanova-wildcats', 'providence-friars', df, model)
#predictWinner('villanova-wildcats', 'butler-bulldogs', df, model)
#predictWinner('villanova-wildcats', 'seton-hall-pirates', df, model)
#predictWinner('villanova-wildcats', 'marquette-golden-eagles', df, model)
#predictWinner('villanova-wildcats', 'providence-friars', df, model)
#predictWinner('villanova-wildcats', 'xavier-musketeers', df, model)
#predictWinner('villanova-wildcats', 'st-johns-red-storm', df, model)


getHomeAwayMarginOfVictory<- function( team_name, df) {
    # Determine indexes that involve team.
	win_index = which(df$win_team == team_name)
	loss_index = which(df$loss_team == team_name)
	
	# What were the win and loss margins?
	win_margin = df$win_points_scored[win_index] - df$loss_points[win_index]
	loss_margin = df$loss_points[loss_index] - df$win_points_scored[loss_index]
	
	# What courts were used?
	win_loss = c('home', 'away')
	win_court = ifelse(df$win_court[win_index] == win_loss[1], win_loss[1], win_loss[2])
	loss_court = ifelse(df$win_court[loss_index] == 'home', win_loss[2], win_loss[1])

	margin = c(win_margin, loss_margin)
	court = c(win_court, loss_court)
	court = as.factor(court)
	df_team = data.frame(margin, court)
	
	return(df_team)
}

getHomeCountAdvantage <- function( team_name, df) {
	df_team = getHomeAwayMarginOfVictory(team_name, df)
	mdl = aov(margin ~ court, data=df_team)
	
	x = summary.lm(mdl)
	
	home_court_advantage = x$coefficients[1,1] + x$coefficients[2,1]
	probability = x$coefficients[2,4]
	
	alist = list('home_court_advantage'=home_court_advantage,
		'probability'=probability)
		
	return(alist)
}

plotHomeCountAdvantage <- function( team_name, df) {
	df_team = getHomeAwayMarginOfVictory(team_name, df)
	alist = getHomeCountAdvantage(team_name, df)
	home_court_advantage = alist$home_court_advantage
	probability = as.integer(alist$probability)
	
	significance = ifelse(probability < 0.05, 'significant', 'not significant')
	
	grand_mean = mean(df_team$margin)
	mean_margin_by_court = tapply(df_team$margin, df_team$court, mean)
	home_mean = mean_margin_by_court['home']
	away_mean = mean_margin_by_court['away']
	title = sprintf("Margin of victory against D1 opponents: %s", team_name)
	# x axis values are just an index.
	x = seq(1, length(df_team$margin))
	
	# Initially plot blanks just to initialize.
	ylabel = sprintf("Home court advantage: %2.0f (%s)", home_court_advantage, significance)
	plot(x, df_team$margin[x], main=title, xlab='game', ylab=ylabel, type='n')
	legend("topright", legend=c('home', 'away'), col=c('green', 'red'), pch=c(17,25))
	
	# Plot the mean lines.
	abline(h=0)
	abline(h=grand_mean)
	abline(h=home_mean, col='green')
	abline(h=away_mean, col='red')
	
	# Get indexes for home and away courts.
	home_index = which(df_team$court == 'home')
	away_index = which(df_team$court == 'away')
	
	# Plot points for home and away indexes.
	points(home_index, df_team$margin[home_index], col='green', pch=17)
	points(away_index, df_team$margin[away_index], col='red', pch=25)
}


plotOffensiveRating <- function( team_name, other_team_name, df) {
	# Get the offensive rating for each team in both win and loss results.
	# Get the relevant rows from the dataframe argument.
	
	# Create a subset dataframe.					  
	dfprime = subset(df, 
		select=c(win_team, win_offensive_rating, loss_team, loss_offensive_rating),
		subset=(win_team == team_name | loss_team == team_name |
		        win_team == other_team_name | loss_team == other_team_name))
	
	# Create labels for the legend.
	team_win_label = sprintf("%s win", team_name)
	team_loss_label = sprintf("%s loss", team_name)
	other_team_win_label = sprintf("%s win", other_team_name)
	other_team_loss_label = sprintf("%s loss", other_team_name)
	title_label = sprintf("Offensive ratings of %s and %s", team_name, other_team_name)
	
	# Plot points for team win and loss indexes.
	team_win_rows = which(dfprime$win_team == team_name)
	team_loss_rows = which(dfprime$loss_team == team_name)
	other_win_rows = which(dfprime$win_team == other_team_name)
	other_loss_rows = which(dfprime$loss_team == other_team_name)
	
	# Create initial plot data.
	x = c(team_win_rows, team_loss_rows, other_win_rows, other_loss_rows) 
	offensive_rating_list = c(
		dfprime$win_offensive_rating[team_win_rows],
		dfprime$loss_offensive_rating[team_loss_rows],
		dfprime$win_offensive_rating[other_win_rows],
		dfprime$loss_offensive_rating[other_loss_rows] )
	
	# Initially plot blanks just to initialize the graph.
	plot(x, offensive_rating_list, main=title_label, xlab='', ylab='offensive_rating', type='n')
	legend("topright", 
			legend=c(team_win_label, team_loss_label, 
			         other_team_win_label, other_team_loss_label), 
			col=c('green', 'red', 'blue', 'orange'), 
			pch=c(2, 6, 3, 4))
	
	points(team_win_rows, dfprime$win_offensive_rating[team_win_rows], col='green', pch=2)
	points(team_loss_rows, dfprime$loss_offensive_rating[team_loss_rows], col='red', pch=6)
	points(other_win_rows, dfprime$win_offensive_rating[other_win_rows], col='blue', pch=3)
	points(other_loss_rows, dfprime$loss_offensive_rating[other_loss_rows], col='red', pch=4)
}

plotDefensiveRating <- function( team_name, other_team_name, df) {
	# Get the defensive rating for each team in both win and loss results.
	# Get the relevant rows from the dataframe argument.
	# Create a subset dataframe.					  
	dfprime = subset(df, 
		select=c(win_team, win_defensive_rating, loss_team, loss_defensive_rating),
		subset=(win_team == team_name | loss_team == team_name |
		        win_team == other_team_name | loss_team == other_team_name))
	
	# Create labels for the legend.
	team_win_label = sprintf("%s win", team_name)
	team_loss_label = sprintf("%s loss", team_name)
	other_team_win_label = sprintf("%s win", other_team_name)
	other_team_loss_label = sprintf("%s loss", other_team_name)
	title_label = sprintf("Defensive ratings of %s and %s", team_name, other_team_name)
	
	# Plot points for team win and loss indexes.
	team_win_rows = which(dfprime$win_team == team_name)
	team_loss_rows = which(dfprime$loss_team == team_name)
	other_win_rows = which(dfprime$win_team == other_team_name)
	other_loss_rows = which(dfprime$loss_team == other_team_name)
	
	# Create initial plot data.
	x = c(team_win_rows, team_loss_rows, other_win_rows, other_loss_rows) 
	defensive_rating_list = c(
		dfprime$win_defensive_rating[team_win_rows],
		dfprime$loss_defensive_rating[team_loss_rows],
		dfprime$win_defensive_rating[other_win_rows],
		dfprime$loss_defensive_rating[other_loss_rows] )
	
	# Initially plot blanks just to initialize the graph.
	plot(x, defensive_rating_list, main=title_label, xlab='', ylab='defensive_rating', type='n')
	legend("topright", 
			legend=c(team_win_label, team_loss_label, 
			         other_team_win_label, other_team_loss_label), 
			col=c('green', 'red', 'blue', 'orange'), 
			pch=c(2, 6, 3, 4))
	
	points(team_win_rows, dfprime$win_defensive_rating[team_win_rows], col='green', pch=2)
	points(team_loss_rows, dfprime$loss_defensive_rating[team_loss_rows], col='red', pch=6)
	points(other_win_rows, dfprime$win_defensive_rating[other_win_rows], col='blue', pch=3)
	points(other_loss_rows, dfprime$loss_defensive_rating[other_loss_rows], col='red', pch=4)
}

# Bracket couples:
# 1-16
# 8-9
# 5-12
# 4-13
# 6-11
# 3-14
# 7-10
# 2-15
# Top 16 tournament 2015-01-26.
# predictWinner('kentucky-wildcats', 'maryland-terrapins', df, model)
# predictWinner('notre-dame-fighting-irish', 'kansas-jayhawks', df, model)
# predictWinner('wisconsin-badgers', 'wichita-state-shockers', df, model)
# predictWinner('duke-blue-devils', 'north-carolina-tar-heels', df, model)
# predictWinner('arizona-wildcats', 'utah-runnin-utes', df, model)
# predictWinner('gonzaga-bulldogs', 'vcu-rams', df, model)
# predictWinner('villanova-wildcats', 'louisville-cardinals', df, model)
# predictWinner('iowa-state-cyclones', 'virginia-cavaliers', df, model)