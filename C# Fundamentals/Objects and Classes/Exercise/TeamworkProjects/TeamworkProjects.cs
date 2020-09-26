using System;
using System.Linq;
using System.Collections.Generic;

namespace TeamworkProjects
{
    class TeamworkProjects
    {

        static void Main(string[] args)
        {
            int teamsCount = int.Parse(Console.ReadLine());
            List<Team> teams = new List<Team>();
            for (int i = 0; i < teamsCount; i++)
            {
                string[] newTeam = Console.ReadLine().Split('-').ToArray();
                List<string> membersList = new List<string>();
                Team team = new Team();
                team.TeamName = newTeam[1];
                team.CreatorName = newTeam[0];
                team.Members = membersList;
                if (!teams.Select(x => x.TeamName).Contains(team.TeamName))
                {
                    if (!teams.Select(x => x.CreatorName).Contains(team.CreatorName))
                    {
                        teams.Add(team);
                        Console.WriteLine("Team {0} has been created by {1}!", newTeam[1], newTeam[0]);
                    }
                    else
                    {
                        Console.WriteLine("{0} cannot create another team!", team.CreatorName);
                    }
                }
                else
                {
                    Console.WriteLine("Team {0} was already created!", team.TeamName);
                }
            }

            string teamRegistration = Console.ReadLine();

            while (!teamRegistration.Equals("end of assignment"))
            {
                var split = teamRegistration.Split(new char[] { '-', '>' }).ToArray();
                string newUser = split[0];
                string teamName = split[2];
                if (!teams.Select(x => x.TeamName).Contains(teamName))
                {
                    Console.WriteLine("Team {0} does not exist!", teamName);
                }
                else if (teams.Select(x => x.Members).Any(x => x.Contains(newUser)) || teams.Select(x => x.CreatorName).Contains(newUser))
                {
                    Console.WriteLine("Member {0} cannot join team {1}!", newUser, teamName);
                }
                else
                {
                    int teamToJoinIndex = teams.FindIndex(x => x.TeamName == teamName);
                    teams[teamToJoinIndex].Members.Add(newUser);
                }

                teamRegistration = Console.ReadLine();
            }

            var teamsToDisband = teams.OrderBy(x => x.TeamName).Where(x => x.Members.Count == 0);
            var fullTeams = teams.
            OrderByDescending(x => x.Members.Count).
            ThenBy(x => x.TeamName).
            Where(x => x.Members.Count > 0);

            foreach (var team in fullTeams)
            {
                Console.WriteLine($"{team.TeamName}");
                Console.WriteLine($"- {team.CreatorName}");
                foreach (var member in team.Members.OrderBy(x => x))
                {
                    Console.WriteLine($"-- {member}");
                }
            }

            Console.WriteLine("Teams to disband:");
            foreach (var item in teamsToDisband)
            {
                Console.WriteLine(item.TeamName);
            }


            //    int countOfTeams = int.Parse(Console.ReadLine());
            //    var creatingTeamList = new List<RegisterTeam>();
            //    var joiningTeamList = new List<JoinTeam>();

            //    string command = Console.ReadLine();

            //    for (int i = 0; i < countOfTeams; i++)
            //    {
            //        string[] teamCreating = command.Split("-");
            //        PrintingTheTeams(teamCreating, creatingTeamList);
            //        command = Console.ReadLine();
            //    }

            //    while (command != "end of assignment")
            //    {                
            //        string[] joiningTeams = command.Split("->");
            //        PrintIfUserJoinTeam(joiningTeams, joiningTeamList, creatingTeamList);

            //        command = Console.ReadLine();
            //    }

            //    List<string> disbandTeam = new List<string>();
            //    var fullTeams = new List<JoinTeam>();
            //    fullTeams = joiningTeamList.OrderBy(o => o.UserName.Count).ThenBy(x => x.Temas).
            //    Where(x => x.UserName.Count > 0).ToList();

            //    foreach (RegisterTeam register in creatingTeamList)
            //    {
            //        if (IsMemmberIsOnlyOne(joiningTeamList, register) == false)
            //        {
            //            disbandTeam.Add(register.TeamName);
            //        }
            //        else
            //        {
            //            Console.WriteLine(register.TeamName);
            //            Console.WriteLine($"- {register.Creator}");

            //            foreach (JoinTeam join in fullTeams)
            //            {
            //                if (join.JoinedTeam == register.TeamName)
            //                {
            //                    Console.WriteLine($"-- {join.UserName}");
            //                }
            //            }
            //        }
            //    }

            //    disbandTeam.Sort();
            //    Console.WriteLine("Teams to disband:");
            //    if(disbandTeam.Count > 0)
            //    {
            //        Console.WriteLine(string.Join(Environment.NewLine, disbandTeam));
            //    }
            //}

            //static bool IsTeamCreatingExist(string teamName, List<RegisterTeam> creatingTeamList)
            //{
            //    foreach(RegisterTeam team in creatingTeamList)
            //    {
            //        if(team.TeamName == teamName)
            //        {
            //            return true;
            //        }
            //    }

            //    return false;
            //}

            //static bool IsCreaterExist(string creatorName, List<RegisterTeam> creatingTeamList)
            //{
            //    foreach (RegisterTeam team in creatingTeamList)
            //    {
            //        if (team.Creator == creatorName)
            //        {
            //            return true;
            //        }
            //    }

            //    return false;
            //}

            //static bool IfTeamExist(List<RegisterTeam> creatingTeamList, string joinedTeam)
            //{
            //    foreach(RegisterTeam team in creatingTeamList)
            //    {
            //        if(team.TeamName == joinedTeam)
            //        {
            //            return true;
            //        }
            //    }

            //    return false;
            //}

            //static bool IfAMemeberAlreadyJoinedATeam(List<RegisterTeam> creatingTeamList, 
            //    string userName,
            //    List<JoinTeam> joiningTeamList)
            //{
            //    foreach(RegisterTeam team in creatingTeamList)
            //    {
            //        if(team.Creator == userName)
            //        {
            //            return true;
            //        }
            //    }

            //    foreach(JoinTeam team in joiningTeamList)
            //    {
            //        if(team.UserName.ToString() == userName)
            //        {
            //            return true;
            //        }
            //    }

            //    return false;
            //}

            //static void PrintingTheTeams(string[] teamCreating, List<RegisterTeam> creatingTeamList)
            //{
            //    string creatorName = teamCreating[0];
            //    string teamName = teamCreating[1];

            //    if (IsTeamCreatingExist(teamName, creatingTeamList) == true || IsCreaterExist(creatorName, creatingTeamList) == true)
            //    {
            //        if (IsTeamCreatingExist(teamName, creatingTeamList) == true)
            //        {
            //            Console.WriteLine($"Team {teamName} was already created!");
            //        }
            //        else
            //        {
            //            Console.WriteLine($"{creatorName} cannot create another team!");
            //        }
            //    }
            //    else
            //    {
            //        RegisterTeam team = new RegisterTeam()
            //        {
            //            Creator = creatorName,
            //            TeamName = teamName
            //        };

            //        creatingTeamList.Add(team);

            //        JoinTeam join = new JoinTeam()
            //        {
            //            Temas = teamName
            //        };

            //        Console.WriteLine($"Team {teamName} has been created by {creatorName}!");
            //    }
            //}

            //static void PrintIfUserJoinTeam(string[] joiningTeams, 
            //    List<JoinTeam> joiningTeamList,
            //    List<RegisterTeam> creatingTeamList)
            //{
            //    string userName = joiningTeams[0];
            //    string joinedTeam = joiningTeams[1];

            //    if(IfTeamExist(creatingTeamList, joinedTeam) == false)
            //    {
            //        Console.WriteLine($"Team {joinedTeam} does not exist!");
            //    }
            //    else if(IfAMemeberAlreadyJoinedATeam(creatingTeamList, userName, joiningTeamList) == true){
            //        Console.WriteLine($"Member {userName} cannot join team {joinedTeam}!");
            //    }
            //    else
            //    {
            //        JoinTeam team = new JoinTeam()
            //        {
            //            JoinedTeam = joinedTeam
            //        };

            //        joiningTeamList.Add(team);
            //        team.UserName.Add(userName);
            //    }
            //}

            //static bool IsMemmberIsOnlyOne(List<JoinTeam> joiningTeamList,
            //    RegisterTeam register)
            //{
            //    foreach(JoinTeam team in joiningTeamList)
            //    {
            //        if(register.TeamName == team.JoinedTeam)
            //        {
            //            return true;
            //        }
            //    }

            //    return false;
        }
    }
}
