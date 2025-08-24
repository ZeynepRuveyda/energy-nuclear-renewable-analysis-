#!/usr/bin/env python3
"""
Basit Kaya Gazı (Shale Gas) Analizi
EU27 vs ABD: Doğal Gaz Trendleri
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# Turkish character support and visual settings
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10
sns.set_theme(style='whitegrid', palette='husl')

def main():
    """Ana fonksiyon"""
    print("🌍 EU27 vs ABD: Basit Kaya Gazı (Shale Gas) Analizi")
    print("="*60)
    
    try:
        # Load data
        data_path = Path.cwd() / 'data' / 'raw' / 'owid-energy-data.csv'
        df = pd.read_csv(data_path)
        
        print(f"✅ Data loaded: {len(df)} total records")
        
        # Filter for EU27 and US
        eu_us_data = df[df['country'].isin(['European Union (27)', 'United States'])]
        eu_us_data = eu_us_data.rename(columns={'country': 'region'})
        eu_us_data.loc[eu_us_data['region'] == 'European Union (27)', 'region'] = 'EU27'
        
        print(f"🌍 Found {len(eu_us_data)} records for EU27 and US")
        
        # Check available columns
        print(f"📊 Available columns: {list(eu_us_data.columns)}")
        
        # Check gas data availability
        gas_columns = [col for col in eu_us_data.columns if 'gas' in col.lower()]
        print(f"⛽ Gas columns: {gas_columns}")
        
        # Check data for each region
        for region in ['EU27', 'US']:
            region_data = eu_us_data[eu_us_data['region'] == region]
            print(f"\n🌍 {region}:")
            print(f"   Records: {len(region_data)}")
            if 'gas_share_energy' in region_data.columns:
                gas_data = region_data['gas_share_energy'].dropna()
                print(f"   Gas share data: {len(gas_data)} records")
                if len(gas_data) > 0:
                    print(f"   Years: {gas_data.index.min()} - {gas_data.index.max()}")
        
        # Create simple visualization if data exists
        if 'gas_share_energy' in eu_us_data.columns:
            print("\n📈 Creating gas share visualization...")
            
            # Filter for years with data
            gas_data = eu_us_data[eu_us_data['gas_share_energy'].notna()].copy()
            
            if len(gas_data) > 0:
                fig, ax = plt.subplots(figsize=(14, 8))
                
                for region in gas_data['region'].unique():
                    region_data = gas_data[gas_data['region'] == region]
                    ax.plot(region_data['year'], region_data['gas_share_energy'], 
                           linewidth=3, marker='o', markersize=4, label=region)
                
                ax.set_title('⛽ Natural Gas Share in Energy Mix', fontsize=16, fontweight='bold')
                ax.set_ylabel('Energy Share (%)', fontsize=14)
                ax.set_xlabel('Year', fontsize=14)
                ax.legend()
                ax.grid(True, alpha=0.3)
                ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x:.1f}%'))
                
                plt.tight_layout()
                plt.savefig('reports/simple_gas_analysis.png', dpi=300, bbox_inches='tight')
                plt.show()
                
                print("✅ Visualization created successfully!")
            else:
                print("❌ No gas data available for visualization")
        else:
            print("❌ Gas share column not found in data")
        
        print("\n✅ Simple shale gas analysis completed!")
        
    except Exception as e:
        print(f"❌ Error during analysis: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())

