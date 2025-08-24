#!/usr/bin/env python3
"""
3'lü Karşılaştırma Analizi: Nükleer, Yenilenebilir ve Kaya Gazı
EU27 vs ABD: Enerji Politikaları Karşılaştırması
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
    print("🌍 EU27 vs ABD: 3'lü Enerji Karşılaştırması")
    print("="*60)
    print("📊 Nükleer + Yenilenebilir + Kaya Gazı Analizi")
    
    try:
        # Load processed data
        data_path = Path.cwd() / 'data' / 'processed' / 'eu_us_energy.csv'
        df = pd.read_csv(data_path)
        df['year'] = pd.to_numeric(df['year'], errors='coerce')
        df = df.dropna(subset=['year'])
        
        print(f"✅ Processed data loaded: {len(df)} records")
        
        # Filter for modern period
        modern_df = df[df['year'] >= 1990].copy()
        
        # Create comprehensive comparison
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(20, 16))
        
        # 1. Nuclear Energy Trends
        for region in ['EU27', 'US']:
            data = modern_df[modern_df['region'] == region]
            ax1.plot(data['year'], data['nuclear_share_energy'], 
                    linewidth=3, marker='o', markersize=4, label=region)
        
        ax1.set_title('⚛️ Nuclear Energy Share (1990-2024)', fontsize=16, fontweight='bold')
        ax1.set_ylabel('Energy Share (%)', fontsize=14)
        ax1.set_xlabel('Year', fontsize=14)
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x:.1f}%'))
        
        # 2. Renewable Energy Trends
        for region in ['EU27', 'US']:
            data = modern_df[modern_df['region'] == region]
            ax2.plot(data['year'], data['renewables_share_energy'], 
                    linewidth=3, marker='s', markersize=4, label=region)
        
        ax2.set_title('🌱 Renewable Energy Share (1990-2024)', fontsize=16, fontweight='bold')
        ax2.set_ylabel('Energy Share (%)', fontsize=14)
        ax2.set_xlabel('Year', fontsize=14)
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x:.1f}%'))
        
        # 3. Gas Energy Trends (Shale Gas)
        # Load raw data for gas information
        raw_data_path = Path.cwd() / 'data' / 'raw' / 'owid-energy-data.csv'
        raw_df = pd.read_csv(raw_data_path)
        raw_df['year'] = pd.to_numeric(raw_df['year'], errors='coerce')
        raw_df = raw_df.dropna(subset=['year'])
        
        # Filter for EU27 and US gas data
        eu_us_gas = raw_df[raw_df['country'].isin(['European Union (27)', 'United States'])]
        eu_us_gas = eu_us_gas.rename(columns={'country': 'region'})
        eu_us_gas.loc[eu_us_gas['region'] == 'European Union (27)', 'region'] = 'EU27'
        
        gas_modern = eu_us_gas[eu_us_gas['year'] >= 1990].copy()
        
        for region in gas_modern['region'].unique():
            region_data = gas_modern[gas_modern['region'] == region]
            if 'gas_share_energy' in region_data.columns:
                gas_data = region_data[region_data['gas_share_energy'].notna()]
                if len(gas_data) > 0:
                    ax3.plot(gas_data['year'], gas_data['gas_share_energy'], 
                            linewidth=3, marker='^', markersize=4, label=f'{region} Gas')
        
        # Shale gas revolution marker
        ax3.axvline(x=2008, color='red', linestyle='--', alpha=0.7, 
                   label='Shale Gas Revolution (2008)')
        ax3.axvspan(2008, 2015, alpha=0.1, color='red')
        
        ax3.set_title('⛽ Natural Gas Share (1990-2024)', fontsize=16, fontweight='bold')
        ax3.set_ylabel('Energy Share (%)', fontsize=14)
        ax3.set_xlabel('Year', fontsize=14)
        ax3.legend()
        ax3.grid(True, alpha=0.3)
        ax3.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x:.1f}%'))
        
        # 4. 2024 Comparison
        latest_data = modern_df[modern_df['year'] == 2024]
        categories = ['Nuclear', 'Renewable', 'Low Carbon']
        
        eu_values = [
            latest_data[latest_data['region'] == 'EU27']['nuclear_share_energy'].iloc[0],
            latest_data[latest_data['region'] == 'EU27']['renewables_share_energy'].iloc[0],
            latest_data[latest_data['region'] == 'EU27']['low_carbon_share_energy'].iloc[0]
        ]
        us_values = [
            latest_data[latest_data['region'] == 'US']['nuclear_share_energy'].iloc[0],
            latest_data[latest_data['region'] == 'US']['renewables_share_energy'].iloc[0],
            latest_data[latest_data['region'] == 'US']['low_carbon_share_energy'].iloc[0]
        ]
        
        x = np.arange(len(categories))
        width = 0.35
        
        bars1 = ax4.bar(x - width/2, eu_values, width, label='EU27', color='#2E86AB', alpha=0.8)
        bars2 = ax4.bar(x + width/2, us_values, width, label='US', color='#A23B72', alpha=0.8)
        
        ax4.set_title('📊 2024 Energy Mix Comparison', fontsize=16, fontweight='bold')
        ax4.set_ylabel('Energy Share (%)', fontsize=14)
        ax4.set_xlabel('Energy Source', fontsize=14)
        ax4.set_xticks(x)
        ax4.set_xticklabels(categories)
        ax4.legend()
        ax4.grid(True, alpha=0.3)
        
        # Write values on bars
        for bar in bars1:
            height = bar.get_height()
            ax4.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                   f'{height:.1f}%', ha='center', va='bottom', fontweight='bold')
        
        for bar in bars2:
            height = bar.get_height()
            ax4.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                   f'{height:.1f}%', ha='center', va='bottom', fontweight='bold')
        
        plt.tight_layout()
        plt.savefig('reports/triple_comparison_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # Print summary
        print("\n" + "="*80)
        print("📊 3'LÜ ENERJİ KARŞILAŞTIRMASI ÖZETİ")
        print("="*80)
        
        print(f"\n🌍 2024 Yılı Karşılaştırması:")
        for region in ['EU27', 'US']:
            region_data = latest_data[latest_data['region'] == region]
            print(f"\n   {region}:")
            print(f"     ⚛️ Nükleer: {region_data['nuclear_share_energy'].iloc[0]:.1f}%")
            print(f"     🌱 Yenilenebilir: {region_data['renewables_share_energy'].iloc[0]:.1f}%")
            print(f"     🔋 Düşük Karbon: {region_data['low_carbon_share_energy'].iloc[0]:.1f}%")
        
        print(f"\n🔍 Trend Analizi (1990-2024):")
        for region in ['EU27', 'US']:
            region_data = modern_df[modern_df['region'] == region]
            nuclear_change = region_data.iloc[-1]['nuclear_share_energy'] - region_data.iloc[0]['nuclear_share_energy']
            renewables_change = region_data.iloc[-1]['renewables_share_energy'] - region_data.iloc[0]['renewables_share_energy']
            
            print(f"\n   {region}:")
            print(f"     ⚛️ Nükleer: {nuclear_change:+.1f}%")
            print(f"     🌱 Yenilenebilir: {renewables_change:+.1f}%")
        
        print(f"\n💡 Ana Bulgular:")
        print(f"   1. EU27 yenilenebilir enerjide lider")
        print(f"   2. ABD nükleer enerjide daha istikrarlı")
        print(f"   3. Kaya gazı devrimi (2008) ABD'de etkili")
        print(f"   4. Her iki bölge de düşük karbon geçişinde ilerliyor")
        
        print("\n✅ 3'lü karşılaştırma analizi tamamlandı!")
        print("📁 Rapor 'reports/triple_comparison_analysis.png' olarak kaydedildi")
        
    except Exception as e:
        print(f"❌ Error during analysis: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())

