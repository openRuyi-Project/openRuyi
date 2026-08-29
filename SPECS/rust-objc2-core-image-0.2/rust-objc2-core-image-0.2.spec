# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name objc2-core-image
%global full_version 0.2.2
%global pkgname objc2-core-image-0.2

Name:           rust-objc2-core-image-0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Rust crate "objc2-core-image"
License:        MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:55260963a527c99f1819c4f8e3b47fe04f9650694ef348ffd2227e8196d34c80
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(objc2-0.5) >= 0.5.2
Requires:       crate(objc2-foundation-0.2) >= 0.2.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/apple) = %{version}
Provides:       crate(%{pkgname}/cikernelmetallib) = %{version}
Provides:       crate(%{pkgname}/ciplugininterface) = %{version}
Provides:       crate(%{pkgname}/coreimagedefines) = %{version}

%description
Source code for takopackized Rust crate "objc2-core-image"

%package     -n %{name}+cibarcodedescriptor
Summary:        Bindings to the CoreImage framework - feature "CIBarcodeDescriptor"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsuseractivity) >= 0.2.2
Provides:       crate(%{pkgname}/cibarcodedescriptor) = %{version}

%description -n %{name}+cibarcodedescriptor
This metapackage enables feature "CIBarcodeDescriptor" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cicolor
Summary:        Bindings to the CoreImage framework - feature "CIColor" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/cicolor) = %{version}
Provides:       crate(%{pkgname}/civector) = %{version}

%description -n %{name}+cicolor
This metapackage enables feature "CIColor" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CIVector" feature.

%package     -n %{name}+cicontext
Summary:        Bindings to the CoreImage framework - feature "CIContext"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Requires:       crate(objc2-metal-0.2/mtlcommandqueue) >= 0.2.2
Requires:       crate(objc2-metal-0.2/mtldevice) >= 0.2.2
Provides:       crate(%{pkgname}/cicontext) = %{version}

%description -n %{name}+cicontext
This metapackage enables feature "CIContext" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cidetector
Summary:        Bindings to the CoreImage framework - feature "CIDetector"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/cidetector) = %{version}

%description -n %{name}+cidetector
This metapackage enables feature "CIDetector" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cifeature
Summary:        Bindings to the CoreImage framework - feature "CIFeature"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/cifeature) = %{version}

%description -n %{name}+cifeature
This metapackage enables feature "CIFeature" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cifilter
Summary:        Bindings to the CoreImage framework - feature "CIFilter" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/cifilter) = %{version}
Provides:       crate(%{pkgname}/cirawfilter) = %{version}

%description -n %{name}+cifilter
This metapackage enables feature "CIFilter" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CIRAWFilter" feature.

%package     -n %{name}+cifilterconstructor
Summary:        Bindings to the CoreImage framework - feature "CIFilterConstructor" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/cifilterconstructor) = %{version}
Provides:       crate(%{pkgname}/ciimageprovider) = %{version}

%description -n %{name}+cifilterconstructor
This metapackage enables feature "CIFilterConstructor" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CIImageProvider" feature.

%package     -n %{name}+cifiltergenerator
Summary:        Bindings to the CoreImage framework - feature "CIFilterGenerator"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/cifiltergenerator) = %{version}

%description -n %{name}+cifiltergenerator
This metapackage enables feature "CIFilterGenerator" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cifiltershape
Summary:        Bindings to the CoreImage framework - feature "CIFilterShape"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Provides:       crate(%{pkgname}/cifiltershape) = %{version}

%description -n %{name}+cifiltershape
This metapackage enables feature "CIFilterShape" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ciimage
Summary:        Bindings to the CoreImage framework - feature "CIImage"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Requires:       crate(objc2-metal-0.2/mtlresource) >= 0.2.2
Requires:       crate(objc2-metal-0.2/mtltexture) >= 0.2.2
Provides:       crate(%{pkgname}/ciimage) = %{version}

%description -n %{name}+ciimage
This metapackage enables feature "CIImage" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ciimageaccumulator
Summary:        Bindings to the CoreImage framework - feature "CIImageAccumulator"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Provides:       crate(%{pkgname}/ciimageaccumulator) = %{version}

%description -n %{name}+ciimageaccumulator
This metapackage enables feature "CIImageAccumulator" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ciimageprocessor
Summary:        Bindings to the CoreImage framework - feature "CIImageProcessor"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-metal-0.2/mtlcommandbuffer) >= 0.2.2
Requires:       crate(objc2-metal-0.2/mtlresource) >= 0.2.2
Requires:       crate(objc2-metal-0.2/mtltexture) >= 0.2.2
Provides:       crate(%{pkgname}/ciimageprocessor) = %{version}

%description -n %{name}+ciimageprocessor
This metapackage enables feature "CIImageProcessor" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cikernel
Summary:        Bindings to the CoreImage framework - feature "CIKernel"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/cikernel) = %{version}

%description -n %{name}+cikernel
This metapackage enables feature "CIKernel" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ciplugin
Summary:        Bindings to the CoreImage framework - feature "CIPlugIn"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/ciplugin) = %{version}

%description -n %{name}+ciplugin
This metapackage enables feature "CIPlugIn" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cirawfilter-deprecated
Summary:        Bindings to the CoreImage framework - feature "CIRAWFilter_Deprecated"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/cirawfilter-deprecated) = %{version}

%description -n %{name}+cirawfilter-deprecated
This metapackage enables feature "CIRAWFilter_Deprecated" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cirenderdestination
Summary:        Bindings to the CoreImage framework - feature "CIRenderDestination"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsdate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-metal-0.2/mtlcommandbuffer) >= 0.2.2
Requires:       crate(objc2-metal-0.2/mtlpixelformat) >= 0.2.2
Requires:       crate(objc2-metal-0.2/mtlresource) >= 0.2.2
Requires:       crate(objc2-metal-0.2/mtltexture) >= 0.2.2
Provides:       crate(%{pkgname}/cirenderdestination) = %{version}

%description -n %{name}+cirenderdestination
This metapackage enables feature "CIRenderDestination" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cisampler
Summary:        Bindings to the CoreImage framework - feature "CISampler"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/cisampler) = %{version}

%description -n %{name}+cisampler
This metapackage enables feature "CISampler" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+all
Summary:        Bindings to the CoreImage framework - feature "all"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/block2) = %{version}
Requires:       crate(%{pkgname}/cibarcodedescriptor) = %{version}
Requires:       crate(%{pkgname}/cicolor) = %{version}
Requires:       crate(%{pkgname}/cicontext) = %{version}
Requires:       crate(%{pkgname}/cidetector) = %{version}
Requires:       crate(%{pkgname}/cifeature) = %{version}
Requires:       crate(%{pkgname}/cifilter) = %{version}
Requires:       crate(%{pkgname}/cifilterconstructor) = %{version}
Requires:       crate(%{pkgname}/cifiltergenerator) = %{version}
Requires:       crate(%{pkgname}/cifiltershape) = %{version}
Requires:       crate(%{pkgname}/ciimage) = %{version}
Requires:       crate(%{pkgname}/ciimageaccumulator) = %{version}
Requires:       crate(%{pkgname}/ciimageprocessor) = %{version}
Requires:       crate(%{pkgname}/ciimageprovider) = %{version}
Requires:       crate(%{pkgname}/cikernel) = %{version}
Requires:       crate(%{pkgname}/cikernelmetallib) = %{version}
Requires:       crate(%{pkgname}/ciplugin) = %{version}
Requires:       crate(%{pkgname}/ciplugininterface) = %{version}
Requires:       crate(%{pkgname}/cirawfilter) = %{version}
Requires:       crate(%{pkgname}/cirawfilter-deprecated) = %{version}
Requires:       crate(%{pkgname}/cirenderdestination) = %{version}
Requires:       crate(%{pkgname}/cisampler) = %{version}
Requires:       crate(%{pkgname}/civector) = %{version}
Requires:       crate(%{pkgname}/coreimagedefines) = %{version}
Requires:       crate(%{pkgname}/objc2-metal) = %{version}
Provides:       crate(%{pkgname}/all) = %{version}

%description -n %{name}+all
This metapackage enables feature "all" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+alloc
Summary:        Bindings to the CoreImage framework - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block2-0.5/alloc) >= 0.5.1
Requires:       crate(objc2-0.5/alloc) >= 0.5.2
Requires:       crate(objc2-foundation-0.2/alloc) >= 0.2.2
Requires:       crate(objc2-metal-0.2/alloc) >= 0.2.2
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+block2
Summary:        Bindings to the CoreImage framework - feature "block2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block2-0.5) >= 0.5.1
Requires:       crate(objc2-foundation-0.2/block2) >= 0.2.2
Requires:       crate(objc2-metal-0.2/block2) >= 0.2.2
Provides:       crate(%{pkgname}/block2) = %{version}

%description -n %{name}+block2
This metapackage enables feature "block2" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnustep-1-7
Summary:        Bindings to the CoreImage framework - feature "gnustep-1-7"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block2-0.5/gnustep-1-7) >= 0.5.1
Requires:       crate(objc2-0.5/gnustep-1-7) >= 0.5.2
Requires:       crate(objc2-foundation-0.2/gnustep-1-7) >= 0.2.2
Provides:       crate(%{pkgname}/gnustep-1-7) = %{version}

%description -n %{name}+gnustep-1-7
This metapackage enables feature "gnustep-1-7" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnustep-1-8
Summary:        Bindings to the CoreImage framework - feature "gnustep-1-8"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gnustep-1-7) = %{version}
Requires:       crate(block2-0.5/gnustep-1-8) >= 0.5.1
Requires:       crate(objc2-0.5/gnustep-1-8) >= 0.5.2
Requires:       crate(objc2-foundation-0.2/gnustep-1-8) >= 0.2.2
Provides:       crate(%{pkgname}/gnustep-1-8) = %{version}

%description -n %{name}+gnustep-1-8
This metapackage enables feature "gnustep-1-8" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnustep-1-9
Summary:        Bindings to the CoreImage framework - feature "gnustep-1-9"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gnustep-1-8) = %{version}
Requires:       crate(block2-0.5/gnustep-1-9) >= 0.5.1
Requires:       crate(objc2-0.5/gnustep-1-9) >= 0.5.2
Requires:       crate(objc2-foundation-0.2/gnustep-1-9) >= 0.2.2
Provides:       crate(%{pkgname}/gnustep-1-9) = %{version}

%description -n %{name}+gnustep-1-9
This metapackage enables feature "gnustep-1-9" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnustep-2-0
Summary:        Bindings to the CoreImage framework - feature "gnustep-2-0"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gnustep-1-9) = %{version}
Requires:       crate(block2-0.5/gnustep-2-0) >= 0.5.1
Requires:       crate(objc2-0.5/gnustep-2-0) >= 0.5.2
Requires:       crate(objc2-foundation-0.2/gnustep-2-0) >= 0.2.2
Provides:       crate(%{pkgname}/gnustep-2-0) = %{version}

%description -n %{name}+gnustep-2-0
This metapackage enables feature "gnustep-2-0" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnustep-2-1
Summary:        Bindings to the CoreImage framework - feature "gnustep-2-1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gnustep-2-0) = %{version}
Requires:       crate(block2-0.5/gnustep-2-1) >= 0.5.1
Requires:       crate(objc2-0.5/gnustep-2-1) >= 0.5.2
Requires:       crate(objc2-foundation-0.2/gnustep-2-1) >= 0.2.2
Provides:       crate(%{pkgname}/gnustep-2-1) = %{version}

%description -n %{name}+gnustep-2-1
This metapackage enables feature "gnustep-2-1" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-metal
Summary:        Bindings to the CoreImage framework - feature "objc2-metal"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-metal-0.2) >= 0.2.2
Provides:       crate(%{pkgname}/objc2-metal) = %{version}

%description -n %{name}+objc2-metal
This metapackage enables feature "objc2-metal" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Bindings to the CoreImage framework - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(block2-0.5/std) >= 0.5.1
Requires:       crate(objc2-0.5/std) >= 0.5.2
Requires:       crate(objc2-foundation-0.2/std) >= 0.2.2
Requires:       crate(objc2-metal-0.2/std) >= 0.2.2
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust objc2-core-image crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
