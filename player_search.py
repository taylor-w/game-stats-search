def main():
    # imports
    import requests
    import json
    import constants

    # input: global vars
    trackergg_key = constants.trackergg_api_key
    apexlegendsapi_key = constants.apexlegendsapi_key

    # input: end-user input vars
    print("Enter Apex platform, i.e) PC, PS4, X1:")
    platform = input()
    print("Enter player name:")
    player = input()

    # input: request header vars
    apexlegendsapi_header = {
        "Authorization": apexlegendsapi_key
    }

    # input: apexlegendsapi request url vars
    apex_player = f'https://api.mozambiquehe.re/bridge?auth={apexlegendsapi_key}&player={player}&platform={platform}'

    # process: request data
    res = requests.get(url=apex_player, params=apexlegendsapi_header)

    # process: massage data
    res_data = res.content.decode("utf-8")
    json_data = json.loads(res_data)

    # # output: pretty print
    # print(json.dumps(json_data, indent=4))

    # output: print desired results
    # apex platform data
    apex_platform = json_data["global"]["platform"]
    apex_season = json_data["global"]["rank"]["rankedSeason"]
    player_name = json_data["global"]["name"]
    apex_level = json_data["global"]["level"]
    apex_rank = f'{json_data["global"]["rank"]["rankName"]} {json_data["global"]["rank"]["rankDiv"]}'
    apex_rank_img = json_data["global"]["rank"]["rankImg"]
    apex_global_data = {
        "Platform": apex_platform,
        "Season": apex_season,
        "Player": player_name,
        "Level": apex_level,
        "Rank": apex_rank
    }
    # apex real time legend data
    selected_legend = json_data["realtime"]["selectedLegend"]
    is_online = json_data["realtime"]["isOnline"]
    is_in_Game = json_data["realtime"]["isInGame"]
    apex_realtime_data = {
        "Selected Legend": selected_legend,
        "Online Status": is_online,
        "In Game Status": is_in_Game
    }
    # apex selected legend data
    selected_legend_name = json_data["legends"]["selected"]["LegendName"]
    selected_legend_data = json_data["legends"]["selected"]["data"]
    apex_selected_legend_data = {
        "Selected Legend": selected_legend_name,
        "Selected Legend Data": selected_legend_data
    }
    # apex all legend data
    all_legend_data = json_data["legends"]["all"]
    apex_played_legend_data = {}
    # process: access played legend data
    for legend in all_legend_data:
        if "data" in all_legend_data[legend]:
            # debug: validate all_legend_data dict
            # print(legend)
            # print(apex_played_legend_data)
            # print(all_legend_data[legend]["data"])
            apex_played_legend_data[legend] = all_legend_data[legend]["data"]

    # output: apex legends v1 data pull
    print(json.dumps(apex_global_data, indent=4))
    print(json.dumps(apex_realtime_data, indent=4))
    print(json.dumps(apex_selected_legend_data, indent=4))
    print(json.dumps(apex_played_legend_data, indent=4))

    # debug: show data types
    # print(f'Test res content type: {type(res2.content)}')
    # print(f'Test res data type: {type(res_data)}')
    # print(f'Test json data type: {type(json_data)}')