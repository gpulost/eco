import json
import pandas as pd
from datetime import datetime

def convert_yahoo_data_to_csv(json_file, csv_file):
    """
    将Yahoo Finance的JSON数据转换为CSV格式
    参考用户提供的表格样式：日期、开市、最高、最低、关盘、调整后的收市价、成交量
    """
    
    # 读取JSON数据
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # 提取数据
    result = data['chart']['result'][0]
    timestamps = result['timestamp']
    quote_data = result['indicators']['quote'][0]
    
    # 获取OHLCV数据
    opens = quote_data['open']
    highs = quote_data['high'] 
    lows = quote_data['low']
    closes = quote_data['close']
    volumes = quote_data['volume']
    
    # 获取调整后收盘价（如果存在）
    adj_closes = result['indicators'].get('adjclose', [{}])[0].get('adjclose', closes)
    
    # 创建DataFrame
    df_data = []
    
    for i in range(len(timestamps)):
        # 将时间戳转换为日期
        date = datetime.fromtimestamp(timestamps[i]).strftime('%Y年%m月%d日')
        
        # 处理None值，保留2位小数
        open_price = round(opens[i], 2) if opens[i] is not None else None
        high_price = round(highs[i], 2) if highs[i] is not None else None
        low_price = round(lows[i], 2) if lows[i] is not None else None
        close_price = round(closes[i], 2) if closes[i] is not None else None
        adj_close_price = round(adj_closes[i], 2) if adj_closes[i] is not None else close_price
        volume = int(volumes[i]) if volumes[i] is not None and volumes[i] > 0 else None
        
        df_data.append({
            '日期': date,
            '开市': open_price,
            '最高': high_price,  
            '最低': low_price,
            '关盘': close_price,
            '调整后的收市价': adj_close_price,
            '成交量': volume
        })
    
    # 创建DataFrame并按日期排序（最新的在前）
    df = pd.DataFrame(df_data)
    df = df.sort_values('日期', ascending=False)
    
    # 保存为CSV
    df.to_csv(csv_file, index=False, encoding='utf-8-sig')
    
    print(f"成功转换 {len(df)} 条记录到 {csv_file}")
    print("\n前5行数据预览：")
    print(df.head())
    
    return df

if __name__ == "__main__":
    # 转换数据
    df = convert_yahoo_data_to_csv('ss.json', 'shanghai_index.csv')