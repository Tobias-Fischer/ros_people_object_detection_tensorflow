# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_detection/protos/preprocessor.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*object_detection/protos/preprocessor.proto\x12\x17object_detection.protos\"\xea\x10\n\x11PreprocessingStep\x12\x42\n\x0fnormalize_image\x18\x01 \x01(\x0b\x32\'.object_detection.protos.NormalizeImageH\x00\x12O\n\x16random_horizontal_flip\x18\x02 \x01(\x0b\x32-.object_detection.protos.RandomHorizontalFlipH\x00\x12R\n\x18random_pixel_value_scale\x18\x03 \x01(\x0b\x32..object_detection.protos.RandomPixelValueScaleH\x00\x12G\n\x12random_image_scale\x18\x04 \x01(\x0b\x32).object_detection.protos.RandomImageScaleH\x00\x12\x46\n\x12random_rgb_to_gray\x18\x05 \x01(\x0b\x32(.object_detection.protos.RandomRGBtoGrayH\x00\x12S\n\x18random_adjust_brightness\x18\x06 \x01(\x0b\x32/.object_detection.protos.RandomAdjustBrightnessH\x00\x12O\n\x16random_adjust_contrast\x18\x07 \x01(\x0b\x32-.object_detection.protos.RandomAdjustContrastH\x00\x12\x45\n\x11random_adjust_hue\x18\x08 \x01(\x0b\x32(.object_detection.protos.RandomAdjustHueH\x00\x12S\n\x18random_adjust_saturation\x18\t \x01(\x0b\x32/.object_detection.protos.RandomAdjustSaturationH\x00\x12K\n\x14random_distort_color\x18\n \x01(\x0b\x32+.object_detection.protos.RandomDistortColorH\x00\x12I\n\x13random_jitter_boxes\x18\x0b \x01(\x0b\x32*.object_detection.protos.RandomJitterBoxesH\x00\x12\x45\n\x11random_crop_image\x18\x0c \x01(\x0b\x32(.object_detection.protos.RandomCropImageH\x00\x12\x43\n\x10random_pad_image\x18\r \x01(\x0b\x32\'.object_detection.protos.RandomPadImageH\x00\x12L\n\x15random_crop_pad_image\x18\x0e \x01(\x0b\x32+.object_detection.protos.RandomCropPadImageH\x00\x12W\n\x1brandom_crop_to_aspect_ratio\x18\x0f \x01(\x0b\x32\x30.object_detection.protos.RandomCropToAspectRatioH\x00\x12K\n\x14random_black_patches\x18\x10 \x01(\x0b\x32+.object_detection.protos.RandomBlackPatchesH\x00\x12K\n\x14random_resize_method\x18\x11 \x01(\x0b\x32+.object_detection.protos.RandomResizeMethodH\x00\x12\x61\n scale_boxes_to_pixel_coordinates\x18\x12 \x01(\x0b\x32\x35.object_detection.protos.ScaleBoxesToPixelCoordinatesH\x00\x12<\n\x0cresize_image\x18\x13 \x01(\x0b\x32$.object_detection.protos.ResizeImageH\x00\x12M\n\x15subtract_channel_mean\x18\x14 \x01(\x0b\x32,.object_detection.protos.SubtractChannelMeanH\x00\x12\x41\n\x0fssd_random_crop\x18\x15 \x01(\x0b\x32&.object_detection.protos.SSDRandomCropH\x00\x12H\n\x13ssd_random_crop_pad\x18\x16 \x01(\x0b\x32).object_detection.protos.SSDRandomCropPadH\x00\x12\x64\n\"ssd_random_crop_fixed_aspect_ratio\x18\x17 \x01(\x0b\x32\x36.object_detection.protos.SSDRandomCropFixedAspectRatioH\x00\x12k\n&ssd_random_crop_pad_fixed_aspect_ratio\x18\x18 \x01(\x0b\x32\x39.object_detection.protos.SSDRandomCropPadFixedAspectRatioH\x00\x12K\n\x14random_vertical_flip\x18\x19 \x01(\x0b\x32+.object_detection.protos.RandomVerticalFlipH\x00\x12\x46\n\x11random_rotation90\x18\x1a \x01(\x0b\x32).object_detection.protos.RandomRotation90H\x00\x12\x39\n\x0brgb_to_gray\x18\x1b \x01(\x0b\x32\".object_detection.protos.RGBtoGrayH\x00\x42\x14\n\x12preprocessing_step\"v\n\x0eNormalizeImage\x12\x17\n\x0foriginal_minval\x18\x01 \x01(\x02\x12\x17\n\x0foriginal_maxval\x18\x02 \x01(\x02\x12\x18\n\rtarget_minval\x18\x03 \x01(\x02:\x01\x30\x12\x18\n\rtarget_maxval\x18\x04 \x01(\x02:\x01\x31\"9\n\x14RandomHorizontalFlip\x12!\n\x19keypoint_flip_permutation\x18\x01 \x03(\x05\"7\n\x12RandomVerticalFlip\x12!\n\x19keypoint_flip_permutation\x18\x01 \x03(\x05\"\x12\n\x10RandomRotation90\"A\n\x15RandomPixelValueScale\x12\x13\n\x06minval\x18\x01 \x01(\x02:\x03\x30.9\x12\x13\n\x06maxval\x18\x02 \x01(\x02:\x03\x31.1\"L\n\x10RandomImageScale\x12\x1c\n\x0fmin_scale_ratio\x18\x01 \x01(\x02:\x03\x30.5\x12\x1a\n\x0fmax_scale_ratio\x18\x02 \x01(\x02:\x01\x32\"+\n\x0fRandomRGBtoGray\x12\x18\n\x0bprobability\x18\x01 \x01(\x02:\x03\x30.1\"0\n\x16RandomAdjustBrightness\x12\x16\n\tmax_delta\x18\x01 \x01(\x02:\x03\x30.2\"G\n\x14RandomAdjustContrast\x12\x16\n\tmin_delta\x18\x01 \x01(\x02:\x03\x30.8\x12\x17\n\tmax_delta\x18\x02 \x01(\x02:\x04\x31.25\"*\n\x0fRandomAdjustHue\x12\x17\n\tmax_delta\x18\x01 \x01(\x02:\x04\x30.02\"I\n\x16RandomAdjustSaturation\x12\x16\n\tmin_delta\x18\x01 \x01(\x02:\x03\x30.8\x12\x17\n\tmax_delta\x18\x02 \x01(\x02:\x04\x31.25\",\n\x12RandomDistortColor\x12\x16\n\x0e\x63olor_ordering\x18\x01 \x01(\x05\"(\n\x11RandomJitterBoxes\x12\x13\n\x05ratio\x18\x01 \x01(\x02:\x04\x30.05\"\xd1\x01\n\x0fRandomCropImage\x12\x1d\n\x12min_object_covered\x18\x01 \x01(\x02:\x01\x31\x12\x1e\n\x10min_aspect_ratio\x18\x02 \x01(\x02:\x04\x30.75\x12\x1e\n\x10max_aspect_ratio\x18\x03 \x01(\x02:\x04\x31.33\x12\x15\n\x08min_area\x18\x04 \x01(\x02:\x03\x30.1\x12\x13\n\x08max_area\x18\x05 \x01(\x02:\x01\x31\x12\x1b\n\x0eoverlap_thresh\x18\x06 \x01(\x02:\x03\x30.3\x12\x16\n\x0brandom_coef\x18\x07 \x01(\x02:\x01\x30\"\x89\x01\n\x0eRandomPadImage\x12\x18\n\x10min_image_height\x18\x01 \x01(\x02\x12\x17\n\x0fmin_image_width\x18\x02 \x01(\x02\x12\x18\n\x10max_image_height\x18\x03 \x01(\x02\x12\x17\n\x0fmax_image_width\x18\x04 \x01(\x02\x12\x11\n\tpad_color\x18\x05 \x03(\x02\"\xa5\x02\n\x12RandomCropPadImage\x12\x1d\n\x12min_object_covered\x18\x01 \x01(\x02:\x01\x31\x12\x1e\n\x10min_aspect_ratio\x18\x02 \x01(\x02:\x04\x30.75\x12\x1e\n\x10max_aspect_ratio\x18\x03 \x01(\x02:\x04\x31.33\x12\x15\n\x08min_area\x18\x04 \x01(\x02:\x03\x30.1\x12\x13\n\x08max_area\x18\x05 \x01(\x02:\x01\x31\x12\x1b\n\x0eoverlap_thresh\x18\x06 \x01(\x02:\x03\x30.3\x12\x16\n\x0brandom_coef\x18\x07 \x01(\x02:\x01\x30\x12\x1d\n\x15min_padded_size_ratio\x18\x08 \x03(\x02\x12\x1d\n\x15max_padded_size_ratio\x18\t \x03(\x02\x12\x11\n\tpad_color\x18\n \x03(\x02\"O\n\x17RandomCropToAspectRatio\x12\x17\n\x0c\x61spect_ratio\x18\x01 \x01(\x02:\x01\x31\x12\x1b\n\x0eoverlap_thresh\x18\x02 \x01(\x02:\x03\x30.3\"o\n\x12RandomBlackPatches\x12\x1d\n\x11max_black_patches\x18\x01 \x01(\x05:\x02\x31\x30\x12\x18\n\x0bprobability\x18\x02 \x01(\x02:\x03\x30.5\x12 \n\x13size_to_image_ratio\x18\x03 \x01(\x02:\x03\x30.1\"A\n\x12RandomResizeMethod\x12\x15\n\rtarget_height\x18\x01 \x01(\x02\x12\x14\n\x0ctarget_width\x18\x02 \x01(\x02\"\x0b\n\tRGBtoGray\"\x1e\n\x1cScaleBoxesToPixelCoordinates\"\xc0\x01\n\x0bResizeImage\x12\x12\n\nnew_height\x18\x01 \x01(\x05\x12\x11\n\tnew_width\x18\x02 \x01(\x05\x12\x45\n\x06method\x18\x03 \x01(\x0e\x32+.object_detection.protos.ResizeImage.Method:\x08\x42ILINEAR\"C\n\x06Method\x12\x08\n\x04\x41REA\x10\x01\x12\x0b\n\x07\x42ICUBIC\x10\x02\x12\x0c\n\x08\x42ILINEAR\x10\x03\x12\x14\n\x10NEAREST_NEIGHBOR\x10\x04\"$\n\x13SubtractChannelMean\x12\r\n\x05means\x18\x01 \x03(\x02\"\xb9\x01\n\x16SSDRandomCropOperation\x12\x1a\n\x12min_object_covered\x18\x01 \x01(\x02\x12\x18\n\x10min_aspect_ratio\x18\x02 \x01(\x02\x12\x18\n\x10max_aspect_ratio\x18\x03 \x01(\x02\x12\x10\n\x08min_area\x18\x04 \x01(\x02\x12\x10\n\x08max_area\x18\x05 \x01(\x02\x12\x16\n\x0eoverlap_thresh\x18\x06 \x01(\x02\x12\x13\n\x0brandom_coef\x18\x07 \x01(\x02\"T\n\rSSDRandomCrop\x12\x43\n\noperations\x18\x01 \x03(\x0b\x32/.object_detection.protos.SSDRandomCropOperation\"\xb9\x02\n\x19SSDRandomCropPadOperation\x12\x1a\n\x12min_object_covered\x18\x01 \x01(\x02\x12\x18\n\x10min_aspect_ratio\x18\x02 \x01(\x02\x12\x18\n\x10max_aspect_ratio\x18\x03 \x01(\x02\x12\x10\n\x08min_area\x18\x04 \x01(\x02\x12\x10\n\x08max_area\x18\x05 \x01(\x02\x12\x16\n\x0eoverlap_thresh\x18\x06 \x01(\x02\x12\x13\n\x0brandom_coef\x18\x07 \x01(\x02\x12\x1d\n\x15min_padded_size_ratio\x18\x08 \x03(\x02\x12\x1d\n\x15max_padded_size_ratio\x18\t \x03(\x02\x12\x13\n\x0bpad_color_r\x18\n \x01(\x02\x12\x13\n\x0bpad_color_g\x18\x0b \x01(\x02\x12\x13\n\x0bpad_color_b\x18\x0c \x01(\x02\"Z\n\x10SSDRandomCropPad\x12\x46\n\noperations\x18\x01 \x03(\x0b\x32\x32.object_detection.protos.SSDRandomCropPadOperation\"\x95\x01\n&SSDRandomCropFixedAspectRatioOperation\x12\x1a\n\x12min_object_covered\x18\x01 \x01(\x02\x12\x10\n\x08min_area\x18\x04 \x01(\x02\x12\x10\n\x08max_area\x18\x05 \x01(\x02\x12\x16\n\x0eoverlap_thresh\x18\x06 \x01(\x02\x12\x13\n\x0brandom_coef\x18\x07 \x01(\x02\"\x8d\x01\n\x1dSSDRandomCropFixedAspectRatio\x12S\n\noperations\x18\x01 \x03(\x0b\x32?.object_detection.protos.SSDRandomCropFixedAspectRatioOperation\x12\x17\n\x0c\x61spect_ratio\x18\x02 \x01(\x02:\x01\x31\"\xcc\x01\n)SSDRandomCropPadFixedAspectRatioOperation\x12\x1a\n\x12min_object_covered\x18\x01 \x01(\x02\x12\x18\n\x10min_aspect_ratio\x18\x02 \x01(\x02\x12\x18\n\x10max_aspect_ratio\x18\x03 \x01(\x02\x12\x10\n\x08min_area\x18\x04 \x01(\x02\x12\x10\n\x08max_area\x18\x05 \x01(\x02\x12\x16\n\x0eoverlap_thresh\x18\x06 \x01(\x02\x12\x13\n\x0brandom_coef\x18\x07 \x01(\x02\"\xd1\x01\n SSDRandomCropPadFixedAspectRatio\x12V\n\noperations\x18\x01 \x03(\x0b\x32\x42.object_detection.protos.SSDRandomCropPadFixedAspectRatioOperation\x12\x17\n\x0c\x61spect_ratio\x18\x02 \x01(\x02:\x01\x31\x12\x1d\n\x15min_padded_size_ratio\x18\x03 \x03(\x02\x12\x1d\n\x15max_padded_size_ratio\x18\x04 \x03(\x02')



_PREPROCESSINGSTEP = DESCRIPTOR.message_types_by_name['PreprocessingStep']
_NORMALIZEIMAGE = DESCRIPTOR.message_types_by_name['NormalizeImage']
_RANDOMHORIZONTALFLIP = DESCRIPTOR.message_types_by_name['RandomHorizontalFlip']
_RANDOMVERTICALFLIP = DESCRIPTOR.message_types_by_name['RandomVerticalFlip']
_RANDOMROTATION90 = DESCRIPTOR.message_types_by_name['RandomRotation90']
_RANDOMPIXELVALUESCALE = DESCRIPTOR.message_types_by_name['RandomPixelValueScale']
_RANDOMIMAGESCALE = DESCRIPTOR.message_types_by_name['RandomImageScale']
_RANDOMRGBTOGRAY = DESCRIPTOR.message_types_by_name['RandomRGBtoGray']
_RANDOMADJUSTBRIGHTNESS = DESCRIPTOR.message_types_by_name['RandomAdjustBrightness']
_RANDOMADJUSTCONTRAST = DESCRIPTOR.message_types_by_name['RandomAdjustContrast']
_RANDOMADJUSTHUE = DESCRIPTOR.message_types_by_name['RandomAdjustHue']
_RANDOMADJUSTSATURATION = DESCRIPTOR.message_types_by_name['RandomAdjustSaturation']
_RANDOMDISTORTCOLOR = DESCRIPTOR.message_types_by_name['RandomDistortColor']
_RANDOMJITTERBOXES = DESCRIPTOR.message_types_by_name['RandomJitterBoxes']
_RANDOMCROPIMAGE = DESCRIPTOR.message_types_by_name['RandomCropImage']
_RANDOMPADIMAGE = DESCRIPTOR.message_types_by_name['RandomPadImage']
_RANDOMCROPPADIMAGE = DESCRIPTOR.message_types_by_name['RandomCropPadImage']
_RANDOMCROPTOASPECTRATIO = DESCRIPTOR.message_types_by_name['RandomCropToAspectRatio']
_RANDOMBLACKPATCHES = DESCRIPTOR.message_types_by_name['RandomBlackPatches']
_RANDOMRESIZEMETHOD = DESCRIPTOR.message_types_by_name['RandomResizeMethod']
_RGBTOGRAY = DESCRIPTOR.message_types_by_name['RGBtoGray']
_SCALEBOXESTOPIXELCOORDINATES = DESCRIPTOR.message_types_by_name['ScaleBoxesToPixelCoordinates']
_RESIZEIMAGE = DESCRIPTOR.message_types_by_name['ResizeImage']
_SUBTRACTCHANNELMEAN = DESCRIPTOR.message_types_by_name['SubtractChannelMean']
_SSDRANDOMCROPOPERATION = DESCRIPTOR.message_types_by_name['SSDRandomCropOperation']
_SSDRANDOMCROP = DESCRIPTOR.message_types_by_name['SSDRandomCrop']
_SSDRANDOMCROPPADOPERATION = DESCRIPTOR.message_types_by_name['SSDRandomCropPadOperation']
_SSDRANDOMCROPPAD = DESCRIPTOR.message_types_by_name['SSDRandomCropPad']
_SSDRANDOMCROPFIXEDASPECTRATIOOPERATION = DESCRIPTOR.message_types_by_name['SSDRandomCropFixedAspectRatioOperation']
_SSDRANDOMCROPFIXEDASPECTRATIO = DESCRIPTOR.message_types_by_name['SSDRandomCropFixedAspectRatio']
_SSDRANDOMCROPPADFIXEDASPECTRATIOOPERATION = DESCRIPTOR.message_types_by_name['SSDRandomCropPadFixedAspectRatioOperation']
_SSDRANDOMCROPPADFIXEDASPECTRATIO = DESCRIPTOR.message_types_by_name['SSDRandomCropPadFixedAspectRatio']
_RESIZEIMAGE_METHOD = _RESIZEIMAGE.enum_types_by_name['Method']
PreprocessingStep = _reflection.GeneratedProtocolMessageType('PreprocessingStep', (_message.Message,), {
  'DESCRIPTOR' : _PREPROCESSINGSTEP,
  '__module__' : 'object_detection.protos.preprocessor_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.PreprocessingStep)
  })
_sym_db.RegisterMessage(PreprocessingStep)

NormalizeImage = _reflection.GeneratedProtocolMessageType('NormalizeImage', (_message.Message,), {
  'DESCRIPTOR' : _NORMALIZEIMAGE,
  '__module__' : 'object_detection.protos.preprocessor_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.NormalizeImage)
  })
_sym_db.RegisterMessage(NormalizeImage)

RandomHorizontalFlip = _reflection.GeneratedProtocolMessageType('RandomHorizontalFlip', (_message.Message,), {
  'DESCRIPTOR' : _RANDOMHORIZONTALFLIP,
  '__module__' : 'object_detection.protos.preprocessor_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.RandomHorizontalFlip)
  })
_sym_db.RegisterMessage(RandomHorizontalFlip)

RandomVerticalFlip = _reflection.GeneratedProtocolMessageType('RandomVerticalFlip', (_message.Message,), {
  'DESCRIPTOR' : _RANDOMVERTICALFLIP,
  '__module__' : 'object_detection.protos.preprocessor_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.RandomVerticalFlip)
  })
_sym_db.RegisterMessage(RandomVerticalFlip)

RandomRotation90 = _reflection.GeneratedProtocolMessageType('RandomRotation90', (_message.Message,), {
  'DESCRIPTOR' : _RANDOMROTATION90,
  '__module__' : 'object_detection.protos.preprocessor_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.RandomRotation90)
  })
_sym_db.RegisterMessage(RandomRotation90)

RandomPixelValueScale = _reflection.GeneratedProtocolMessageType('RandomPixelValueScale', (_message.Message,), {
  'DESCRIPTOR' : _RANDOMPIXELVALUESCALE,
  '__module__' : 'object_detection.protos.preprocessor_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.RandomPixelValueScale)
  })
_sym_db.RegisterMessage(RandomPixelValueScale)

RandomImageScale = _reflection.GeneratedProtocolMessageType('RandomImageScale', (_message.Message,), {
  'DESCRIPTOR' : _RANDOMIMAGESCALE,
  '__module__' : 'object_detection.protos.preprocessor_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.RandomImageScale)
  })
_sym_db.RegisterMessage(RandomImageScale)

RandomRGBtoGray = _reflection.GeneratedProtocolMessageType('RandomRGBtoGray', (_message.Message,), {
  'DESCRIPTOR' : _RANDOMRGBTOGRAY,
  '__module__' : 'object_detection.protos.preprocessor_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.RandomRGBtoGray)
  })
_sym_db.RegisterMessage(RandomRGBtoGray)

RandomAdjustBrightness = _reflection.GeneratedProtocolMessageType('RandomAdjustBrightness', (_message.Message,), {
  'DESCRIPTOR' : _RANDOMADJUSTBRIGHTNESS,
  '__module__' : 'object_detection.protos.preprocessor_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.RandomAdjustBrightness)
  })
_sym_db.RegisterMessage(RandomAdjustBrightness)

RandomAdjustContrast = _reflection.GeneratedProtocolMessageType('RandomAdjustContrast', (_message.Message,), {
  'DESCRIPTOR' : _RANDOMADJUSTCONTRAST,
  '__module__' : 'object_detection.protos.preprocessor_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.RandomAdjustContrast)
  })
_sym_db.RegisterMessage(RandomAdjustContrast)

RandomAdjustHue = _reflection.GeneratedProtocolMessageType('RandomAdjustHue', (_message.Message,), {
  'DESCRIPTOR' : _RANDOMADJUSTHUE,
  '__module__' : 'object_detection.protos.preprocessor_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.RandomAdjustHue)
  })
_sym_db.RegisterMessage(RandomAdjustHue)

RandomAdjustSaturation = _reflection.GeneratedProtocolMessageType('RandomAdjustSaturation', (_message.Message,), {
  'DESCRIPTOR' : _RANDOMADJUSTSATURATION,
  '__module__' : 'object_detection.protos.preprocessor_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.RandomAdjustSaturation)
  })
_sym_db.RegisterMessage(RandomAdjustSaturation)

RandomDistortColor = _reflection.GeneratedProtocolMessageType('RandomDistortColor', (_message.Message,), {
  'DESCRIPTOR' : _RANDOMDISTORTCOLOR,
  '__module__' : 'object_detection.protos.preprocessor_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.RandomDistortColor)
  })
_sym_db.RegisterMessage(RandomDistortColor)

RandomJitterBoxes = _reflection.GeneratedProtocolMessageType('RandomJitterBoxes', (_message.Message,), {
  'DESCRIPTOR' : _RANDOMJITTERBOXES,
  '__module__' : 'object_detection.protos.preprocessor_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.RandomJitterBoxes)
  })
_sym_db.RegisterMessage(RandomJitterBoxes)

RandomCropImage = _reflection.GeneratedProtocolMessageType('RandomCropImage', (_message.Message,), {
  'DESCRIPTOR' : _RANDOMCROPIMAGE,
  '__module__' : 'object_detection.protos.preprocessor_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.RandomCropImage)
  })
_sym_db.RegisterMessage(RandomCropImage)

RandomPadImage = _reflection.GeneratedProtocolMessageType('RandomPadImage', (_message.Message,), {
  'DESCRIPTOR' : _RANDOMPADIMAGE,
  '__module__' : 'object_detection.protos.preprocessor_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.RandomPadImage)
  })
_sym_db.RegisterMessage(RandomPadImage)

RandomCropPadImage = _reflection.GeneratedProtocolMessageType('RandomCropPadImage', (_message.Message,), {
  'DESCRIPTOR' : _RANDOMCROPPADIMAGE,
  '__module__' : 'object_detection.protos.preprocessor_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.RandomCropPadImage)
  })
_sym_db.RegisterMessage(RandomCropPadImage)

RandomCropToAspectRatio = _reflection.GeneratedProtocolMessageType('RandomCropToAspectRatio', (_message.Message,), {
  'DESCRIPTOR' : _RANDOMCROPTOASPECTRATIO,
  '__module__' : 'object_detection.protos.preprocessor_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.RandomCropToAspectRatio)
  })
_sym_db.RegisterMessage(RandomCropToAspectRatio)

RandomBlackPatches = _reflection.GeneratedProtocolMessageType('RandomBlackPatches', (_message.Message,), {
  'DESCRIPTOR' : _RANDOMBLACKPATCHES,
  '__module__' : 'object_detection.protos.preprocessor_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.RandomBlackPatches)
  })
_sym_db.RegisterMessage(RandomBlackPatches)

RandomResizeMethod = _reflection.GeneratedProtocolMessageType('RandomResizeMethod', (_message.Message,), {
  'DESCRIPTOR' : _RANDOMRESIZEMETHOD,
  '__module__' : 'object_detection.protos.preprocessor_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.RandomResizeMethod)
  })
_sym_db.RegisterMessage(RandomResizeMethod)

RGBtoGray = _reflection.GeneratedProtocolMessageType('RGBtoGray', (_message.Message,), {
  'DESCRIPTOR' : _RGBTOGRAY,
  '__module__' : 'object_detection.protos.preprocessor_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.RGBtoGray)
  })
_sym_db.RegisterMessage(RGBtoGray)

ScaleBoxesToPixelCoordinates = _reflection.GeneratedProtocolMessageType('ScaleBoxesToPixelCoordinates', (_message.Message,), {
  'DESCRIPTOR' : _SCALEBOXESTOPIXELCOORDINATES,
  '__module__' : 'object_detection.protos.preprocessor_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.ScaleBoxesToPixelCoordinates)
  })
_sym_db.RegisterMessage(ScaleBoxesToPixelCoordinates)

ResizeImage = _reflection.GeneratedProtocolMessageType('ResizeImage', (_message.Message,), {
  'DESCRIPTOR' : _RESIZEIMAGE,
  '__module__' : 'object_detection.protos.preprocessor_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.ResizeImage)
  })
_sym_db.RegisterMessage(ResizeImage)

SubtractChannelMean = _reflection.GeneratedProtocolMessageType('SubtractChannelMean', (_message.Message,), {
  'DESCRIPTOR' : _SUBTRACTCHANNELMEAN,
  '__module__' : 'object_detection.protos.preprocessor_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.SubtractChannelMean)
  })
_sym_db.RegisterMessage(SubtractChannelMean)

SSDRandomCropOperation = _reflection.GeneratedProtocolMessageType('SSDRandomCropOperation', (_message.Message,), {
  'DESCRIPTOR' : _SSDRANDOMCROPOPERATION,
  '__module__' : 'object_detection.protos.preprocessor_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.SSDRandomCropOperation)
  })
_sym_db.RegisterMessage(SSDRandomCropOperation)

SSDRandomCrop = _reflection.GeneratedProtocolMessageType('SSDRandomCrop', (_message.Message,), {
  'DESCRIPTOR' : _SSDRANDOMCROP,
  '__module__' : 'object_detection.protos.preprocessor_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.SSDRandomCrop)
  })
_sym_db.RegisterMessage(SSDRandomCrop)

SSDRandomCropPadOperation = _reflection.GeneratedProtocolMessageType('SSDRandomCropPadOperation', (_message.Message,), {
  'DESCRIPTOR' : _SSDRANDOMCROPPADOPERATION,
  '__module__' : 'object_detection.protos.preprocessor_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.SSDRandomCropPadOperation)
  })
_sym_db.RegisterMessage(SSDRandomCropPadOperation)

SSDRandomCropPad = _reflection.GeneratedProtocolMessageType('SSDRandomCropPad', (_message.Message,), {
  'DESCRIPTOR' : _SSDRANDOMCROPPAD,
  '__module__' : 'object_detection.protos.preprocessor_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.SSDRandomCropPad)
  })
_sym_db.RegisterMessage(SSDRandomCropPad)

SSDRandomCropFixedAspectRatioOperation = _reflection.GeneratedProtocolMessageType('SSDRandomCropFixedAspectRatioOperation', (_message.Message,), {
  'DESCRIPTOR' : _SSDRANDOMCROPFIXEDASPECTRATIOOPERATION,
  '__module__' : 'object_detection.protos.preprocessor_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.SSDRandomCropFixedAspectRatioOperation)
  })
_sym_db.RegisterMessage(SSDRandomCropFixedAspectRatioOperation)

SSDRandomCropFixedAspectRatio = _reflection.GeneratedProtocolMessageType('SSDRandomCropFixedAspectRatio', (_message.Message,), {
  'DESCRIPTOR' : _SSDRANDOMCROPFIXEDASPECTRATIO,
  '__module__' : 'object_detection.protos.preprocessor_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.SSDRandomCropFixedAspectRatio)
  })
_sym_db.RegisterMessage(SSDRandomCropFixedAspectRatio)

SSDRandomCropPadFixedAspectRatioOperation = _reflection.GeneratedProtocolMessageType('SSDRandomCropPadFixedAspectRatioOperation', (_message.Message,), {
  'DESCRIPTOR' : _SSDRANDOMCROPPADFIXEDASPECTRATIOOPERATION,
  '__module__' : 'object_detection.protos.preprocessor_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.SSDRandomCropPadFixedAspectRatioOperation)
  })
_sym_db.RegisterMessage(SSDRandomCropPadFixedAspectRatioOperation)

SSDRandomCropPadFixedAspectRatio = _reflection.GeneratedProtocolMessageType('SSDRandomCropPadFixedAspectRatio', (_message.Message,), {
  'DESCRIPTOR' : _SSDRANDOMCROPPADFIXEDASPECTRATIO,
  '__module__' : 'object_detection.protos.preprocessor_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.SSDRandomCropPadFixedAspectRatio)
  })
_sym_db.RegisterMessage(SSDRandomCropPadFixedAspectRatio)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PREPROCESSINGSTEP._serialized_start=72
  _PREPROCESSINGSTEP._serialized_end=2226
  _NORMALIZEIMAGE._serialized_start=2228
  _NORMALIZEIMAGE._serialized_end=2346
  _RANDOMHORIZONTALFLIP._serialized_start=2348
  _RANDOMHORIZONTALFLIP._serialized_end=2405
  _RANDOMVERTICALFLIP._serialized_start=2407
  _RANDOMVERTICALFLIP._serialized_end=2462
  _RANDOMROTATION90._serialized_start=2464
  _RANDOMROTATION90._serialized_end=2482
  _RANDOMPIXELVALUESCALE._serialized_start=2484
  _RANDOMPIXELVALUESCALE._serialized_end=2549
  _RANDOMIMAGESCALE._serialized_start=2551
  _RANDOMIMAGESCALE._serialized_end=2627
  _RANDOMRGBTOGRAY._serialized_start=2629
  _RANDOMRGBTOGRAY._serialized_end=2672
  _RANDOMADJUSTBRIGHTNESS._serialized_start=2674
  _RANDOMADJUSTBRIGHTNESS._serialized_end=2722
  _RANDOMADJUSTCONTRAST._serialized_start=2724
  _RANDOMADJUSTCONTRAST._serialized_end=2795
  _RANDOMADJUSTHUE._serialized_start=2797
  _RANDOMADJUSTHUE._serialized_end=2839
  _RANDOMADJUSTSATURATION._serialized_start=2841
  _RANDOMADJUSTSATURATION._serialized_end=2914
  _RANDOMDISTORTCOLOR._serialized_start=2916
  _RANDOMDISTORTCOLOR._serialized_end=2960
  _RANDOMJITTERBOXES._serialized_start=2962
  _RANDOMJITTERBOXES._serialized_end=3002
  _RANDOMCROPIMAGE._serialized_start=3005
  _RANDOMCROPIMAGE._serialized_end=3214
  _RANDOMPADIMAGE._serialized_start=3217
  _RANDOMPADIMAGE._serialized_end=3354
  _RANDOMCROPPADIMAGE._serialized_start=3357
  _RANDOMCROPPADIMAGE._serialized_end=3650
  _RANDOMCROPTOASPECTRATIO._serialized_start=3652
  _RANDOMCROPTOASPECTRATIO._serialized_end=3731
  _RANDOMBLACKPATCHES._serialized_start=3733
  _RANDOMBLACKPATCHES._serialized_end=3844
  _RANDOMRESIZEMETHOD._serialized_start=3846
  _RANDOMRESIZEMETHOD._serialized_end=3911
  _RGBTOGRAY._serialized_start=3913
  _RGBTOGRAY._serialized_end=3924
  _SCALEBOXESTOPIXELCOORDINATES._serialized_start=3926
  _SCALEBOXESTOPIXELCOORDINATES._serialized_end=3956
  _RESIZEIMAGE._serialized_start=3959
  _RESIZEIMAGE._serialized_end=4151
  _RESIZEIMAGE_METHOD._serialized_start=4084
  _RESIZEIMAGE_METHOD._serialized_end=4151
  _SUBTRACTCHANNELMEAN._serialized_start=4153
  _SUBTRACTCHANNELMEAN._serialized_end=4189
  _SSDRANDOMCROPOPERATION._serialized_start=4192
  _SSDRANDOMCROPOPERATION._serialized_end=4377
  _SSDRANDOMCROP._serialized_start=4379
  _SSDRANDOMCROP._serialized_end=4463
  _SSDRANDOMCROPPADOPERATION._serialized_start=4466
  _SSDRANDOMCROPPADOPERATION._serialized_end=4779
  _SSDRANDOMCROPPAD._serialized_start=4781
  _SSDRANDOMCROPPAD._serialized_end=4871
  _SSDRANDOMCROPFIXEDASPECTRATIOOPERATION._serialized_start=4874
  _SSDRANDOMCROPFIXEDASPECTRATIOOPERATION._serialized_end=5023
  _SSDRANDOMCROPFIXEDASPECTRATIO._serialized_start=5026
  _SSDRANDOMCROPFIXEDASPECTRATIO._serialized_end=5167
  _SSDRANDOMCROPPADFIXEDASPECTRATIOOPERATION._serialized_start=5170
  _SSDRANDOMCROPPADFIXEDASPECTRATIOOPERATION._serialized_end=5374
  _SSDRANDOMCROPPADFIXEDASPECTRATIO._serialized_start=5377
  _SSDRANDOMCROPPADFIXEDASPECTRATIO._serialized_end=5586
# @@protoc_insertion_point(module_scope)
