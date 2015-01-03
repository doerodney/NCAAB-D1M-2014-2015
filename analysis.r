setwd("c:/github/doerodney/NCAAB-D1M-2014-2015")

df = read.csv("dataframe.csv", header=TRUE)

summary(df)

# margin of victory
# df$mov = df$win_points_scored - df$loss_points_scored

pythagorean_expectation <- function(scored, allowed, n) {
	py_ex = scored^n / (scored^n + allowed^n)
	
	py_ex
}

# remove low contributors
plotFit <- function(yObserved, yFitted, intercept=0) {
  plot(yObserved, yFitted, xlab="Actual", ylab="Predicted")
  abline(intercept, 1, lty=2, col=rgb(1,0,0))
}


#df$Margin = df$PointsScored - df$loss_teamPointsScored
#model <- aov(Margin ~ TeamConference:OpponentConference, data = df)

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
    if (nTeamWins > nOpponentWins) {
        msg = sprintf("%s wins %d scenarios.", teamName, nTeamWins)
    } else {
        msg = sprintf("%s wins %d scenarios.", opponentName, nOpponentWins)
    }
    print(msg)
	
	#return(pointsScored)
}

 predictWinner('villanova-wildcats', 'seton-hall-pirates', df, model)



