import re
import pandas as pd
__builders = dict()
__default_ohlc = ['open', 'high', 'low', 'close']


def __get_file_name(class_name):
    res = re.findall('[A-Z][^A-Z]*', class_name)
    return '_'.join([cur.lower() for cur in res])


def __load_module(module_path):
    p = module_path.rfind('.') + 1
    super_module = module_path[p:]
    try:
        module = __import__(module_path, fromlist=[super_module], level=0)
        return module
    except ImportError as e:
        raise e


def __get_class_by_name(class_name):
    file_name = __get_file_name(class_name)
    mod_name = 'candlestick.patterns.' + file_name

    if mod_name not in __builders:
        module = __load_module(mod_name)
        __builders[mod_name] = module
    else:
        module = __builders[mod_name]
    return getattr(module, class_name)


def __create_object(class_name, target):
    return __get_class_by_name(class_name)(target=target)


def bullish_hanging_man(candles_df,
                   ohlc=__default_ohlc,
                   is_reversed=False,
                   ):
    target='BullishHangingMan'
    pattern = __create_object(target, target)
    pattern = pattern.has_pattern(candles_df, ohlc, is_reversed)
    pattern = pattern.loc[:, target]
    pattern = pattern.astype(bool)
    pattern = pattern.astype(int)
    return pattern
    


def hanging_man(candles_df,
                   ohlc=__default_ohlc,
                   is_reversed=False,
                   ):
    target='HangingMan'
    pattern = __create_object(target, target)
    pattern = pattern.has_pattern(candles_df, ohlc, is_reversed)
    pattern = pattern.loc[:, target]
    pattern = pattern.astype(bool)
    pattern = pattern.astype(int)
    return pattern
   

def bearish_harami(candles_df,
                   ohlc=__default_ohlc,
                   is_reversed=False,
                   ):
    target='BearishHarami'
    pattern = __create_object(target, target)
    pattern = pattern.has_pattern(candles_df, ohlc, is_reversed)
    pattern = pattern.loc[:, target]
    pattern = pattern.astype(bool)
    pattern = pattern.astype(int)
    return pattern


def bullish_harami(candles_df,
                   ohlc=__default_ohlc,
                   is_reversed=False,
                   ):
    target='BullishHarami'
    pattern = __create_object(target, target)
    pattern = pattern.has_pattern(candles_df, ohlc, is_reversed)
    pattern = pattern.loc[:, target]
    pattern = pattern.astype(bool)
    pattern = pattern.astype(int)
    return pattern
    


def gravestone_doji(candles_df,
                   ohlc=__default_ohlc,
                   is_reversed=False,
                   ):
    target='GravestoneDoji'
    pattern = __create_object(target, target)
    pattern = pattern.has_pattern(candles_df, ohlc, is_reversed)
    pattern = pattern.loc[:, target]
    pattern = pattern.astype(bool)
    pattern = pattern.astype(int)
    return pattern
    


def dark_cloud_cover(candles_df,
                     ohlc=__default_ohlc,
                     is_reversed=False,
                     ):
    target='DarkCloudCover'
    pattern = __create_object(target, target)
    pattern = pattern.has_pattern(candles_df, ohlc, is_reversed)
    pattern = pattern.loc[:, target]
    pattern = pattern.astype(bool)
    pattern = pattern.astype(int)
    return pattern
    


def doji(candles_df,
         ohlc=__default_ohlc,
         is_reversed=False,
         ):
    target='Doji'
    pattern = __create_object(target, target)
    pattern = pattern.has_pattern(candles_df, ohlc, is_reversed)
    pattern = pattern.loc[:, target]
    pattern = pattern.astype(bool)
    pattern = pattern.astype(int)
    return pattern
    


def doji_star(candles_df,
              ohlc=__default_ohlc,
              is_reversed=False,
             ):
    target='DojiStar'
    pattern = __create_object(target, target)
    pattern = pattern.has_pattern(candles_df, ohlc, is_reversed)
    pattern = pattern.loc[:, target]
    pattern = pattern.astype(bool)
    pattern = pattern.astype(int)
    return pattern
  


def dragonfly_doji(candles_df,
                   ohlc=__default_ohlc,
                   is_reversed=False,
                   ):
    target='DragonflyDoji'
    pattern = __create_object(target, target)
    pattern = pattern.has_pattern(candles_df, ohlc, is_reversed)
    pattern = pattern.loc[:, target]
    pattern = pattern.astype(bool)
    pattern = pattern.astype(int)
    return pattern
  


def bearish_engulfing(candles_df,
                   ohlc=__default_ohlc,
                   is_reversed=False,
                   ):
    target='BearishEngulfing'
    pattern = __create_object(target, target)
    pattern = pattern.has_pattern(candles_df, ohlc, is_reversed)
    pattern = pattern.loc[:, target]
    pattern = pattern.astype(bool)
    pattern = pattern.astype(int)
    return pattern
    


def bullish_engulfing(candles_df,
                   ohlc=__default_ohlc,
                   is_reversed=False,
                   ):
    target='BullishEngulfing'
    pattern = __create_object(target, target)
    pattern = pattern.has_pattern(candles_df, ohlc, is_reversed)
    pattern = pattern.loc[:, target]
    pattern = pattern.astype(bool)
    pattern = pattern.astype(int)
    return pattern


def hammer(candles_df,
                   ohlc=__default_ohlc,
                   is_reversed=False,
                   ):
    target='Hammer'
    pattern = __create_object(target, target)
    pattern = pattern.has_pattern(candles_df, ohlc, is_reversed)
    pattern = pattern.loc[:, target]
    pattern = pattern.astype(bool)
    pattern = pattern.astype(int)
    return pattern


def inverted_hammer(candles_df,
                   ohlc=__default_ohlc,
                   is_reversed=False,
                   ):
    target='InvertedHammer'
    pattern = __create_object(target, target)
    pattern = pattern.has_pattern(candles_df, ohlc, is_reversed)
    pattern = pattern.loc[:, target]
    pattern = pattern.astype(bool)
    pattern = pattern.astype(int)
    return pattern


def morning_star(candles_df,
                   ohlc=__default_ohlc,
                   is_reversed=False,
                   ):
    target='MorningStar'
    pattern = __create_object(target, target)
    pattern = pattern.has_pattern(candles_df, ohlc, is_reversed)
    pattern = pattern.loc[:, target]
    pattern = pattern.astype(bool)
    pattern = pattern.astype(int)
    return pattern


def morning_star_doji(candles_df,
                   ohlc=__default_ohlc,
                   is_reversed=False,
                   ):
    target='MorningStarDoji'
    pattern = __create_object(target, target)
    pattern = pattern.has_pattern(candles_df, ohlc, is_reversed)
    pattern = pattern.loc[:, target]
    pattern = pattern.astype(bool)
    pattern = pattern.astype(int)
    return pattern


def piercing_pattern(candles_df,
                   ohlc=__default_ohlc,
                   is_reversed=False,
                   ):
    target='PiercingPattern'
    pattern = __create_object(target, target)
    pattern = pattern.has_pattern(candles_df, ohlc, is_reversed)
    pattern = pattern.loc[:, target]
    pattern = pattern.astype(bool)
    pattern = pattern.astype(int)
    return pattern


def rain_drop(candles_df,
                   ohlc=__default_ohlc,
                   is_reversed=False,
                   ):
    target='RainDrop'
    pattern = __create_object(target, target)
    pattern = pattern.has_pattern(candles_df, ohlc, is_reversed)
    pattern = pattern.loc[:, target]
    pattern = pattern.astype(bool)
    pattern = pattern.astype(int)
    return pattern



def rain_drop_doji(candles_df,
                   ohlc=__default_ohlc,
                   is_reversed=False,
                   ):
    target='RainDropDoji'
    pattern = __create_object(target, target)
    pattern = pattern.has_pattern(candles_df, ohlc, is_reversed)
    pattern = pattern.loc[:, target]
    pattern = pattern.astype(bool)
    pattern = pattern.astype(int)
    return pattern

def star(candles_df,
                   ohlc=__default_ohlc,
                   is_reversed=False,
                   ):
    target='Star'
    pattern = __create_object(target, target)
    pattern = pattern.has_pattern(candles_df, ohlc, is_reversed)
    pattern = pattern.loc[:, target]
    pattern = pattern.astype(bool)
    pattern = pattern.astype(int)
    return pattern


def shooting_star(candles_df,
                   ohlc=__default_ohlc,
                   is_reversed=False,
                   ):
    target='ShootingStar'
    pattern = __create_object(target, target)
    pattern = pattern.has_pattern(candles_df, ohlc, is_reversed)
    pattern = pattern.loc[:, target]
    pattern = pattern.astype(bool)
    pattern = pattern.astype(int)
    return pattern
