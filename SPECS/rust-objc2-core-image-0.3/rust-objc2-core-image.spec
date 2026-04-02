# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name objc2-core-image
%global full_version 0.3.2
%global pkgname objc2-core-image-0.3

Name:           rust-objc2-core-image-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "objc2-core-image"
License:        Zlib OR Apache-2.0 OR MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:e5d563b38d2b97209f8e861173de434bd0214cf020e3423a52624cd1d989f006
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(objc2-0.6/std) >= 0.6.4
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/ciimageaccumulator)
Provides:       crate(%{pkgname}/cikernelmetallib)
Provides:       crate(%{pkgname}/ciplugininterface)
Provides:       crate(%{pkgname}/coreimagedefines)
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/unstable-darwin-objc)

%description
Source code for takopackized Rust crate "objc2-core-image"

%package     -n %{name}+cibarcodedescriptor
Summary:        Bindings to the CoreImage framework - feature "CIBarcodeDescriptor"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsuseractivity) >= 0.3.2
Provides:       crate(%{pkgname}/cibarcodedescriptor)

%description -n %{name}+cibarcodedescriptor
This metapackage enables feature "CIBarcodeDescriptor" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cicolor
Summary:        Bindings to the CoreImage framework - feature "CIColor" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/cicolor)
Provides:       crate(%{pkgname}/civector)

%description -n %{name}+cicolor
This metapackage enables feature "CIColor" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CIVector" feature.

%package     -n %{name}+cicontext
Summary:        Bindings to the CoreImage framework - feature "CIContext"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/cicontext)

%description -n %{name}+cicontext
This metapackage enables feature "CIContext" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cidetector
Summary:        Bindings to the CoreImage framework - feature "CIDetector"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/cidetector)

%description -n %{name}+cidetector
This metapackage enables feature "CIDetector" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cifeature
Summary:        Bindings to the CoreImage framework - feature "CIFeature"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/cifeature)

%description -n %{name}+cifeature
This metapackage enables feature "CIFeature" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cifilter
Summary:        Bindings to the CoreImage framework - feature "CIFilter"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/cifilter)

%description -n %{name}+cifilter
This metapackage enables feature "CIFilter" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cifilterbuiltins
Summary:        Bindings to the CoreImage framework - feature "CIFilterBuiltins"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/cifilterbuiltins)

%description -n %{name}+cifilterbuiltins
This metapackage enables feature "CIFilterBuiltins" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cifilterconstructor
Summary:        Bindings to the CoreImage framework - feature "CIFilterConstructor"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/cifilterconstructor)

%description -n %{name}+cifilterconstructor
This metapackage enables feature "CIFilterConstructor" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cifiltergenerator
Summary:        Bindings to the CoreImage framework - feature "CIFilterGenerator"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/cifiltergenerator)

%description -n %{name}+cifiltergenerator
This metapackage enables feature "CIFilterGenerator" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cifiltershape
Summary:        Bindings to the CoreImage framework - feature "CIFilterShape"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/cifiltershape)

%description -n %{name}+cifiltershape
This metapackage enables feature "CIFilterShape" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ciimage
Summary:        Bindings to the CoreImage framework - feature "CIImage" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/ciimage)
Provides:       crate(%{pkgname}/cirawfilter)

%description -n %{name}+ciimage
This metapackage enables feature "CIImage" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CIRAWFilter" feature.

%package     -n %{name}+ciimageprocessor
Summary:        Bindings to the CoreImage framework - feature "CIImageProcessor"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/ciimageprocessor)

%description -n %{name}+ciimageprocessor
This metapackage enables feature "CIImageProcessor" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ciimageprovider
Summary:        Bindings to the CoreImage framework - feature "CIImageProvider"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/ciimageprovider)

%description -n %{name}+ciimageprovider
This metapackage enables feature "CIImageProvider" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cikernel
Summary:        Bindings to the CoreImage framework - feature "CIKernel"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/cikernel)

%description -n %{name}+cikernel
This metapackage enables feature "CIKernel" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ciplugin
Summary:        Bindings to the CoreImage framework - feature "CIPlugIn"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/ciplugin)

%description -n %{name}+ciplugin
This metapackage enables feature "CIPlugIn" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cirawfilter-deprecated
Summary:        Bindings to the CoreImage framework - feature "CIRAWFilter_Deprecated"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/cirawfilter-deprecated)

%description -n %{name}+cirawfilter-deprecated
This metapackage enables feature "CIRAWFilter_Deprecated" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cirenderdestination
Summary:        Bindings to the CoreImage framework - feature "CIRenderDestination"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/cirenderdestination)

%description -n %{name}+cirenderdestination
This metapackage enables feature "CIRenderDestination" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cisampler
Summary:        Bindings to the CoreImage framework - feature "CISampler"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/cisampler)

%description -n %{name}+cisampler
This metapackage enables feature "CISampler" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+block2
Summary:        Bindings to the CoreImage framework - feature "block2"
Requires:       crate(%{pkgname})
Requires:       crate(block2-0.6/alloc) >= 0.6.1
Provides:       crate(%{pkgname}/block2)

%description -n %{name}+block2
This metapackage enables feature "block2" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Bindings to the CoreImage framework - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/block2)
Requires:       crate(%{pkgname}/cibarcodedescriptor)
Requires:       crate(%{pkgname}/cicolor)
Requires:       crate(%{pkgname}/cicontext)
Requires:       crate(%{pkgname}/cidetector)
Requires:       crate(%{pkgname}/cifeature)
Requires:       crate(%{pkgname}/cifilter)
Requires:       crate(%{pkgname}/cifilterbuiltins)
Requires:       crate(%{pkgname}/cifilterconstructor)
Requires:       crate(%{pkgname}/cifiltergenerator)
Requires:       crate(%{pkgname}/cifiltershape)
Requires:       crate(%{pkgname}/ciimage)
Requires:       crate(%{pkgname}/ciimageaccumulator)
Requires:       crate(%{pkgname}/ciimageprocessor)
Requires:       crate(%{pkgname}/ciimageprovider)
Requires:       crate(%{pkgname}/cikernel)
Requires:       crate(%{pkgname}/cikernelmetallib)
Requires:       crate(%{pkgname}/ciplugin)
Requires:       crate(%{pkgname}/ciplugininterface)
Requires:       crate(%{pkgname}/cirawfilter)
Requires:       crate(%{pkgname}/cirawfilter-deprecated)
Requires:       crate(%{pkgname}/cirenderdestination)
Requires:       crate(%{pkgname}/cisampler)
Requires:       crate(%{pkgname}/civector)
Requires:       crate(%{pkgname}/coreimagedefines)
Requires:       crate(%{pkgname}/objc2-core-foundation)
Requires:       crate(%{pkgname}/objc2-core-graphics)
Requires:       crate(%{pkgname}/objc2-core-video)
Requires:       crate(%{pkgname}/objc2-image-io)
Requires:       crate(%{pkgname}/objc2-metal)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnustep-1-7
Summary:        Bindings to the CoreImage framework - feature "gnustep-1-7"
Requires:       crate(%{pkgname})
Requires:       crate(block2-0.6/alloc) >= 0.6.1
Requires:       crate(block2-0.6/gnustep-1-7) >= 0.6.1
Requires:       crate(objc2-0.6/gnustep-1-7) >= 0.6.4
Requires:       crate(objc2-0.6/std) >= 0.6.4
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/gnustep-1-7) >= 0.3.2
Provides:       crate(%{pkgname}/gnustep-1-7)

%description -n %{name}+gnustep-1-7
This metapackage enables feature "gnustep-1-7" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnustep-1-8
Summary:        Bindings to the CoreImage framework - feature "gnustep-1-8"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/gnustep-1-7)
Requires:       crate(block2-0.6/alloc) >= 0.6.1
Requires:       crate(block2-0.6/gnustep-1-8) >= 0.6.1
Requires:       crate(objc2-0.6/gnustep-1-8) >= 0.6.4
Requires:       crate(objc2-0.6/std) >= 0.6.4
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/gnustep-1-8) >= 0.3.2
Provides:       crate(%{pkgname}/gnustep-1-8)

%description -n %{name}+gnustep-1-8
This metapackage enables feature "gnustep-1-8" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnustep-1-9
Summary:        Bindings to the CoreImage framework - feature "gnustep-1-9"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/gnustep-1-8)
Requires:       crate(block2-0.6/alloc) >= 0.6.1
Requires:       crate(block2-0.6/gnustep-1-9) >= 0.6.1
Requires:       crate(objc2-0.6/gnustep-1-9) >= 0.6.4
Requires:       crate(objc2-0.6/std) >= 0.6.4
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/gnustep-1-9) >= 0.3.2
Provides:       crate(%{pkgname}/gnustep-1-9)

%description -n %{name}+gnustep-1-9
This metapackage enables feature "gnustep-1-9" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnustep-2-0
Summary:        Bindings to the CoreImage framework - feature "gnustep-2-0"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/gnustep-1-9)
Requires:       crate(block2-0.6/alloc) >= 0.6.1
Requires:       crate(block2-0.6/gnustep-2-0) >= 0.6.1
Requires:       crate(objc2-0.6/gnustep-2-0) >= 0.6.4
Requires:       crate(objc2-0.6/std) >= 0.6.4
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/gnustep-2-0) >= 0.3.2
Provides:       crate(%{pkgname}/gnustep-2-0)

%description -n %{name}+gnustep-2-0
This metapackage enables feature "gnustep-2-0" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnustep-2-1
Summary:        Bindings to the CoreImage framework - feature "gnustep-2-1"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/gnustep-2-0)
Requires:       crate(block2-0.6/alloc) >= 0.6.1
Requires:       crate(block2-0.6/gnustep-2-1) >= 0.6.1
Requires:       crate(objc2-0.6/gnustep-2-1) >= 0.6.4
Requires:       crate(objc2-0.6/std) >= 0.6.4
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/gnustep-2-1) >= 0.3.2
Provides:       crate(%{pkgname}/gnustep-2-1)

%description -n %{name}+gnustep-2-1
This metapackage enables feature "gnustep-2-1" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-core-foundation
Summary:        Bindings to the CoreImage framework - feature "objc2-core-foundation"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/objc2) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-core-foundation)

%description -n %{name}+objc2-core-foundation
This metapackage enables feature "objc2-core-foundation" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-core-graphics
Summary:        Bindings to the CoreImage framework - feature "objc2-core-graphics"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-core-graphics-0.3/cgcolor) >= 0.3.2
Requires:       crate(objc2-core-graphics-0.3/cgcolorspace) >= 0.3.2
Requires:       crate(objc2-core-graphics-0.3/cgcontext) >= 0.3.2
Requires:       crate(objc2-core-graphics-0.3/cgimage) >= 0.3.2
Requires:       crate(objc2-core-graphics-0.3/cglayer) >= 0.3.2
Requires:       crate(objc2-core-graphics-0.3/objc2) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-core-graphics)

%description -n %{name}+objc2-core-graphics
This metapackage enables feature "objc2-core-graphics" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-core-ml
Summary:        Bindings to the CoreImage framework - feature "objc2-core-ml"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-core-ml-0.3/mlmodel) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-core-ml)

%description -n %{name}+objc2-core-ml
This metapackage enables feature "objc2-core-ml" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-core-video
Summary:        Bindings to the CoreImage framework - feature "objc2-core-video"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-core-video-0.3/cvbuffer) >= 0.3.2
Requires:       crate(objc2-core-video-0.3/cvimagebuffer) >= 0.3.2
Requires:       crate(objc2-core-video-0.3/cvpixelbuffer) >= 0.3.2
Requires:       crate(objc2-core-video-0.3/objc2) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-core-video)

%description -n %{name}+objc2-core-video
This metapackage enables feature "objc2-core-video" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-image-io
Summary:        Bindings to the CoreImage framework - feature "objc2-image-io"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-image-io-0.3/cgimageproperties) >= 0.3.2
Requires:       crate(objc2-image-io-0.3/cgimagesource) >= 0.3.2
Requires:       crate(objc2-image-io-0.3/objc2) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-image-io)

%description -n %{name}+objc2-image-io
This metapackage enables feature "objc2-image-io" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-io-surface
Summary:        Bindings to the CoreImage framework - feature "objc2-io-surface"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-io-surface-0.3/iosurfaceref) >= 0.3.2
Requires:       crate(objc2-io-surface-0.3/objc2) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-io-surface)

%description -n %{name}+objc2-io-surface
This metapackage enables feature "objc2-io-surface" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-metal
Summary:        Bindings to the CoreImage framework - feature "objc2-metal"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-metal-0.3/mtlallocation) >= 0.3.2
Requires:       crate(objc2-metal-0.3/mtlcommandbuffer) >= 0.3.2
Requires:       crate(objc2-metal-0.3/mtlcommandqueue) >= 0.3.2
Requires:       crate(objc2-metal-0.3/mtldevice) >= 0.3.2
Requires:       crate(objc2-metal-0.3/mtlpixelformat) >= 0.3.2
Requires:       crate(objc2-metal-0.3/mtlresource) >= 0.3.2
Requires:       crate(objc2-metal-0.3/mtltexture) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-metal)

%description -n %{name}+objc2-metal
This metapackage enables feature "objc2-metal" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-open-gl
Summary:        Bindings to the CoreImage framework - feature "objc2-open-gl"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-open-gl-0.3/cgltypes) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-open-gl)

%description -n %{name}+objc2-open-gl
This metapackage enables feature "objc2-open-gl" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
