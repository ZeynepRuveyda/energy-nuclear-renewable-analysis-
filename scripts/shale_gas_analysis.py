#!/usr/bin/env python3
"""
Kaya Gazı (Shale Gas) Analizi ve Raporlama
EU27 vs ABD: Doğal Gaz ve Kaya Gazı Trendleri
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

class ShaleGasAnalyzer:
    def __init__(self, data_path: str = None):
        if data_path is None:
            data_path = Path.cwd() / 'data' / 'raw' / 'owid-energy-data.csv'
        
        self.df = pd.read_csv(data_path)
        self.df['year'] = pd.to_numeric(self.df['year'], errors='coerce')
        self.df = self.df.dropna(subset=['year'])
        
        # Filter for EU27 and US
        self.eu_us_data = self.df[self.df['country'].isin(['European Union (27)', 'United States'])]
        self.eu_us_data = self.eu_us_data.rename(columns={'country': 'region'})
        self.eu_us_data.loc[self.eu_us_data['region'] == 'European Union (27)', 'region'] = 'EU27'
        
        # Check if data exists
        if len(self.eu_us_data) == 0:
            raise ValueError("No data found for EU27 and US")
        
        print(f"Found {len(self.eu_us_data)} records for EU27 and US")
        
        # Modern period (post-1990 for shale gas revolution)
        self.modern_df = self.eu_us_data[self.eu_us_data['year'] >= 1990].copy()
        
        print("✅ Shale Gas Analyzer initialized!")
        print(f"📊 Data loaded: {len(self.df)} total records")
        print(f"🌍 Regions: {', '.join(self.eu_us_data['region'].unique())}")
    
    def analyze_natural_gas_trends(self):
        """Doğal gaz trendlerini analiz et"""
        print("\n🔍 Analyzing Natural Gas Trends...")
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))
        
        # Natural gas consumption trends
        for region in ['EU27', 'US']:
            data = self.modern_df[self.modern_df['region'] == region]
            ax1.plot(data['year'], data['gas_consumption'], 
                    linewidth=3, marker='o', markersize=4, label=region)
        
        ax1.set_title('⛽ Natural Gas Consumption (1990-2024)', fontsize=16, fontweight='bold')
        ax1.set_ylabel('Consumption (TWh)', fontsize=14)
        ax1.set_xlabel('Year', fontsize=14)
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Natural gas share in energy mix
        for region in ['EU27', 'US']:
            data = self.modern_df[self.modern_df['region'] == region]
            ax2.plot(data['year'], data['gas_share_energy'], 
                    linewidth=3, marker='s', markersize=4, label=region)
        
        # Shale gas revolution marker (2008-2010)
        ax2.axvline(x=2008, color='red', linestyle='--', alpha=0.7, 
                   label='Shale Gas Revolution (2008)')
        ax2.axvspan(2008, 2015, alpha=0.1, color='red')
        
        ax2.set_title('⛽ Natural Gas Share in Energy Mix (1990-2024)', fontsize=16, fontweight='bold')
        ax2.set_ylabel('Energy Share (%)', fontsize=14)
        ax2.set_xlabel('Year', fontsize=14)
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x:.1f}%'))
        
        plt.tight_layout()
        plt.savefig('reports/shale_gas_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        return fig
    
    def analyze_shale_gas_impact(self):
        """Shale gas etkisini analiz et"""
        print("\n🔍 Analyzing Shale Gas Impact...")
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))
        
        # Pre and post shale gas comparison
        pre_shale = self.modern_df[self.modern_df['year'] <= 2008]
        post_shale = self.modern_df[self.modern_df['year'] > 2008]
        
        regions = ['EU27', 'US']
        pre_values = []
        post_values = []
        
        for region in regions:
            pre_data = pre_shale[pre_shale['region'] == region]['gas_share_energy'].mean()
            post_data = post_shale[post_shale['region'] == region]['gas_share_energy'].mean()
            pre_values.append(pre_data)
            post_values.append(post_data)
            
        print(f"Pre-shale values: {pre_values}")
        print(f"Post-shale values: {post_values}")
        
        # Filter out NaN values
        valid_regions = []
        valid_pre_values = []
        valid_post_values = []
        
        for i, (pre_val, post_val) in enumerate(zip(pre_values, post_values)):
            if not (pd.isna(pre_val) or pd.isna(post_val)):
                valid_regions.append(regions[i])
                valid_pre_values.append(pre_val)
                valid_post_values.append(post_val)
        
        if len(valid_regions) == 0:
            print("No valid data found for comparison")
            return fig
        
        x = np.arange(len(valid_regions))
        width = 0.35
        
        bars1 = ax1.bar(x - width/2, valid_pre_values, width, label='Pre-Shale Gas (1990-2008)', 
                        color='#2E86AB', alpha=0.8)
        bars2 = ax1.bar(x + width/2, valid_post_values, width, label='Post-Shale Gas (2009-2024)', 
                        color='#A23B72', alpha=0.8)
        
        ax1.set_title('⛽ Shale Gas Impact on Natural Gas Share', fontsize=16, fontweight='bold')
        ax1.set_ylabel('Average Gas Share (%)', fontsize=14)
        ax1.set_xlabel('Region', fontsize=14)
        ax1.set_xticks(x)
        ax1.set_xticklabels(valid_regions)
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Write values on bars
        for bar in bars1:
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                   f'{height:.1f}%', ha='center', va='bottom', fontweight='bold')
        
        for bar in bars2:
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                   f'{height:.1f}%', ha='center', va='bottom', fontweight='bold')
        
        # Gas production vs consumption
        for region in ['EU27', 'US']:
            data = self.modern_df[self.modern_df['region'] == region]
            ax2.plot(data['year'], data['gas_production'], 
                    linewidth=3, marker='^', markersize=4, label=f'{region} Production')
            ax2.plot(data['year'], data['gas_consumption'], 
                    linewidth=3, marker='v', markersize=4, label=f'{region} Consumption', linestyle='--')
        
        ax2.set_title('⛽ Gas Production vs Consumption (1990-2024)', fontsize=16, fontweight='bold')
        ax2.set_ylabel('Energy (TWh)', fontsize=14)
        ax2.set_xlabel('Year', fontsize=14)
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('reports/shale_gas_impact.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        return fig
    
    def create_comprehensive_analysis(self):
        """Kapsamlı analiz oluştur"""
        print("\n🚀 Creating comprehensive shale gas analysis...")
        
        # Create main analysis
        fig1 = self.analyze_natural_gas_trends()
        fig2 = self.analyze_shale_gas_impact()
        
        # Create comprehensive figure
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(20, 16))
        
        # 1. Natural gas consumption trends
        for region in ['EU27', 'US']:
            data = self.modern_df[self.modern_df['region'] == region]
            ax1.plot(data['year'], data['gas_consumption'], 
                    linewidth=3, marker='o', markersize=4, label=region)
        
        ax1.set_title('⛽ Natural Gas Consumption Trends', fontsize=16, fontweight='bold')
        ax1.set_ylabel('Consumption (TWh)', fontsize=14)
        ax1.set_xlabel('Year', fontsize=14)
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # 2. Gas share in energy mix
        for region in ['EU27', 'US']:
            data = self.modern_df[self.modern_df['region'] == region]
            ax2.plot(data['year'], data['gas_share_energy'], 
                    linewidth=3, marker='s', markersize=4, label=region)
        
        ax2.axvline(x=2008, color='red', linestyle='--', alpha=0.7, 
                   label='Shale Gas Revolution (2008)')
        ax2.set_title('⛽ Gas Share in Energy Mix', fontsize=16, fontweight='bold')
        ax2.set_ylabel('Energy Share (%)', fontsize=14)
        ax2.set_xlabel('Year', fontsize=14)
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x:.1f}%'))
        
        # 3. Production vs Consumption
        for region in ['EU27', 'US']:
            data = self.modern_df[self.modern_df['region'] == region]
            ax3.plot(data['year'], data['gas_production'], 
                    linewidth=3, marker='^', markersize=4, label=f'{region} Production')
            ax3.plot(data['year'], data['gas_consumption'], 
                    linewidth=3, marker='v', markersize=4, label=f'{region} Consumption', linestyle='--')
        
        ax3.set_title('⛽ Gas Production vs Consumption', fontsize=16, fontweight='bold')
        ax3.set_ylabel('Energy (TWh)', fontsize=14)
        ax3.set_xlabel('Year', fontsize=14)
        ax3.legend()
        ax3.grid(True, alpha=0.3)
        
        # 4. 2024 comparison
        latest_data = self.modern_df[self.modern_df['year'] == 2024]
        categories = ['Gas Share', 'Gas Production', 'Gas Consumption']
        
        eu_values = [
            latest_data[latest_data['region'] == 'EU27']['gas_share_energy'].iloc[0],
            latest_data[latest_data['region'] == 'EU27']['gas_production'].iloc[0] / 100,  # Scale down
            latest_data[latest_data['region'] == 'EU27']['gas_consumption'].iloc[0] / 100
        ]
        us_values = [
            latest_data[latest_data['region'] == 'US']['gas_share_energy'].iloc[0],
            latest_data[latest_data['region'] == 'US']['gas_production'].iloc[0] / 100,
            latest_data[latest_data['region'] == 'US']['gas_consumption'].iloc[0] / 100
        ]
        
        x = np.arange(len(categories))
        width = 0.35
        
        bars1 = ax4.bar(x - width/2, eu_values, width, label='EU27', color='#2E86AB', alpha=0.8)
        bars2 = ax4.bar(x + width/2, us_values, width, label='US', color='#A23B72', alpha=0.8)
        
        ax4.set_title('📊 2024 Gas Metrics Comparison', fontsize=16, fontweight='bold')
        ax4.set_ylabel('Value', fontsize=14)
        ax4.set_xlabel('Metric', fontsize=14)
        ax4.set_xticks(x)
        ax4.set_xticklabels(categories)
        ax4.legend()
        ax4.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('reports/comprehensive_shale_gas_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        print("📈 Comprehensive shale gas analysis completed!")
        return fig
    
    def print_statistical_summary(self):
        """İstatistiksel özet yazdır"""
        print("\n" + "="*80)
        print("📊 SHALE GAS ANALYSIS STATISTICAL SUMMARY")
        print("="*80)
        
        latest_data = self.modern_df[self.modern_df['year'] == 2024]
        
        for region in ['EU27', 'US']:
            region_data = latest_data[latest_data['region'] == region]
            print(f"\n🌍 {region}:")
            print(f"   Natural Gas Share: {region_data['gas_share_energy'].iloc[0]:.1f}%")
            print(f"   Gas Production: {region_data['gas_production'].iloc[0]:.1f} TWh")
            print(f"   Gas Consumption: {region_data['gas_consumption'].iloc[0]:.1f} TWh")
        
        # Shale gas impact analysis
        print(f"\n🔍 SHALE GAS IMPACT ANALYSIS:")
        pre_shale = self.modern_df[self.modern_df['year'] <= 2008]
        post_shale = self.modern_df[self.modern_df['year'] > 2008]
        
        for region in ['EU27', 'US']:
            pre_gas = pre_shale[pre_shale['region'] == region]['gas_share_energy'].mean()
            post_gas = post_shale[post_shale['region'] == region]['gas_share_energy'].mean()
            change = post_gas - pre_gas
            
            print(f"\n   {region}:")
            print(f"     Pre-Shale (1990-2008): {pre_gas:.1f}%")
            print(f"     Post-Shale (2009-2024): {post_gas:.1f}%")
            print(f"     Change: {change:+.1f}%")
    
    def print_policy_recommendations(self):
        """Politika önerileri yazdır"""
        print("\n" + "="*80)
        print("💡 POLICY RECOMMENDATIONS FOR SHALE GAS")
        print("="*80)
        
        print("\n🇪🇺 For EU27:")
        print("   1. Shale gas development: Consider environmental regulations")
        print("   2. Energy security: Diversify gas supply sources")
        print("   3. Infrastructure: Invest in LNG terminals and pipelines")
        print("   4. Technology: Develop cleaner extraction methods")
        
        print("\n🇺🇸 For US:")
        print("   1. Shale gas leadership: Maintain technological advantage")
        print("   2. Export capacity: Expand LNG export infrastructure")
        print("   3. Environmental standards: Improve extraction practices")
        print("   4. Market stability: Balance domestic and export demand")
        
        print("\n🌍 General Recommendations:")
        print("   1. Environmental protection: Strict regulations for fracking")
        print("   2. Technology transfer: Share best practices globally")
        print("   3. Market integration: Develop global gas markets")
        print("   4. Transition planning: Use as bridge fuel to renewables")

def main():
    """Ana fonksiyon"""
    print("🌍 EU27 vs ABD: Kaya Gazı (Shale Gas) Analizi")
    print("="*60)
    
    try:
        # Initialize analyzer
        analyzer = ShaleGasAnalyzer()
        
        # Create comprehensive analysis
        analyzer.create_comprehensive_analysis()
        
        # Print summaries
        analyzer.print_statistical_summary()
        analyzer.print_policy_recommendations()
        
        print("\n✅ Shale gas analysis completed successfully!")
        print("📁 Reports saved in 'reports/' directory")
        
    except Exception as e:
        print(f"❌ Error during analysis: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
