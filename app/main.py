import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# データ読み込み
df = pd.read_csv("datasets/avocado.csv")

# ヒストグラム
plt.figure()
df["AveragePrice"].hist(bins=20, edgecolor="black")
plt.xlabel("Average Price($USD)")
plt.title("Distribution of Avocado Average Price")

plt.savefig("/app/graphs/hist.png")  # 画像を保存

# 散布図
plt.figure()
plt.scatter(df["Total Volume"], df["4225"], alpha=0.5)
plt.xlabel("Total Volume")
plt.ylabel("Soled #4225 Volume")
plt.title("Scatter Plot of Average Price vs Total Bags")

plt.savefig("/app/graphs/scatter.png")

# 平均価格をカテゴリ化（5つの価格帯）
df["Price Category"] = pd.cut(df["AveragePrice"], bins=5, labels=["Very Low", "Low", "Medium", "High", "Very High"])

# 箱ひげ図（価格帯ごとの販売数の分布）
plt.figure()
sns.boxplot(x="Price Category", y="Total Bags", data=df)
plt.xlabel("Average Price Category")
plt.ylabel("Total Bags Sold")
plt.title("Boxplot of Total Bags Sold by Price Category")

plt.savefig("/app/graphs/boxplot.png")

print("\nCOMPLETE!!!\n/graphs 配下にグラフの画像を出力しました。")
