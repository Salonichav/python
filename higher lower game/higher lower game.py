
taylor_swift = 1000
ariana_grande = 380
kylie_jenner = 400
hailey_bieber = 52
kendall_jenner = 295

names = ["Taylor Swift", "Ariana Grande", "Kylie Jenner", "Hailey Bieber", "Kendall Jenner"]
followers = [taylor_swift, ariana_grande, kylie_jenner, hailey_bieber, kendall_jenner]

highest_followers = max(followers)
lowest_followers = min(followers)

highest_index = followers.index(highest_followers)
lowest_index = followers.index(lowest_followers)

print("Instagram Followers:")
print("---------------------")
print("Taylor Swift:", taylor_swift, "M")
print("Ariana Grande:", ariana_grande, "M")
print("Kylie Jenner:", kylie_jenner, "M")
print("Hailey Bieber:", hailey_bieber, "M")
print("Kendall Jenner:", kendall_jenner, "M")

print("\nHighest Followers:", names[highest_index], "-", highest_followers, "M")
print("Lowest Followers:", names[lowest_index], "-", lowest_followers, "M")






