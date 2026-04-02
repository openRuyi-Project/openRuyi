# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name objc2-core-graphics
%global full_version 0.3.2
%global pkgname objc2-core-graphics-0.3

Name:           rust-objc2-core-graphics-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "objc2-core-graphics"
License:        Zlib OR Apache-2.0 OR MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:e022c9d066895efa1345f8e33e584b9f958da2fd4cd116792e15e07e4720a807
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(objc2-core-foundation-0.3) >= 0.3.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/cgbase)
Provides:       crate(%{pkgname}/cgdirectdisplaymetal)
Provides:       crate(%{pkgname}/cgdirectpalette)
Provides:       crate(%{pkgname}/cgdisplayfade)
Provides:       crate(%{pkgname}/cgerror)
Provides:       crate(%{pkgname}/cgitutonemapping)
Provides:       crate(%{pkgname}/cgpdfoperatortable)
Provides:       crate(%{pkgname}/cgwindowlevel)
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/unstable-darwin-objc)

%description
Source code for takopackized Rust crate "objc2-core-graphics"

%package     -n %{name}+cgaffinetransform
Summary:        Bindings to the CoreGraphics framework - feature "CGAffineTransform" and 8 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Provides:       crate(%{pkgname}/cgaffinetransform)
Provides:       crate(%{pkgname}/cgfunction)
Provides:       crate(%{pkgname}/cgpattern)
Provides:       crate(%{pkgname}/cgpdfarray)
Provides:       crate(%{pkgname}/cgpdfdictionary)
Provides:       crate(%{pkgname}/cgpdfobject)
Provides:       crate(%{pkgname}/cgpdfpage)
Provides:       crate(%{pkgname}/cgpdfscanner)
Provides:       crate(%{pkgname}/cgshading)

%description -n %{name}+cgaffinetransform
This metapackage enables feature "CGAffineTransform" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CGFunction", "CGPDFArray", "CGPDFDictionary", "CGPDFObject", "CGPDFPage", "CGPDFScanner", "CGPattern", and "CGShading" features.

%package     -n %{name}+cgbitmapcontext
Summary:        Bindings to the CoreGraphics framework - feature "CGBitmapContext"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-core-foundation-0.3/cfbyteorder) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cferror) >= 0.3.2
Provides:       crate(%{pkgname}/cgbitmapcontext)

%description -n %{name}+cgbitmapcontext
This metapackage enables feature "CGBitmapContext" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cgcolor
Summary:        Bindings to the CoreGraphics framework - feature "CGColor" and 4 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Provides:       crate(%{pkgname}/cgcolor)
Provides:       crate(%{pkgname}/cgcontext)
Provides:       crate(%{pkgname}/cgconvertcolordatawithformat)
Provides:       crate(%{pkgname}/cggeometry)
Provides:       crate(%{pkgname}/cglayer)

%description -n %{name}+cgcolor
This metapackage enables feature "CGColor" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CGContext", "CGConvertColorDataWithFormat", "CGGeometry", and "CGLayer" features.

%package     -n %{name}+cgcolorconversioninfo
Summary:        Bindings to the CoreGraphics framework - feature "CGColorConversionInfo"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cferror) >= 0.3.2
Provides:       crate(%{pkgname}/cgcolorconversioninfo)

%description -n %{name}+cgcolorconversioninfo
This metapackage enables feature "CGColorConversionInfo" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cgcolorspace
Summary:        Bindings to the CoreGraphics framework - feature "CGColorSpace"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdata) >= 0.3.2
Provides:       crate(%{pkgname}/cgcolorspace)

%description -n %{name}+cgcolorspace
This metapackage enables feature "CGColorSpace" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cgdataconsumer
Summary:        Bindings to the CoreGraphics framework - feature "CGDataConsumer" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-core-foundation-0.3/cfdata) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfurl) >= 0.3.2
Provides:       crate(%{pkgname}/cgdataconsumer)
Provides:       crate(%{pkgname}/cgdataprovider)

%description -n %{name}+cgdataconsumer
This metapackage enables feature "CGDataConsumer" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CGDataProvider" feature.

%package     -n %{name}+cgdirectdisplay
Summary:        Bindings to the CoreGraphics framework - feature "CGDirectDisplay"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-core-foundation-0.3/cfarray) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Provides:       crate(%{pkgname}/cgdirectdisplay)

%description -n %{name}+cgdirectdisplay
This metapackage enables feature "CGDirectDisplay" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cgdisplayconfiguration
Summary:        Bindings to the CoreGraphics framework - feature "CGDisplayConfiguration"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Provides:       crate(%{pkgname}/cgdisplayconfiguration)

%description -n %{name}+cgdisplayconfiguration
This metapackage enables feature "CGDisplayConfiguration" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cgdisplaystream
Summary:        Bindings to the CoreGraphics framework - feature "CGDisplayStream"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfrunloop) >= 0.3.2
Provides:       crate(%{pkgname}/cgdisplaystream)

%description -n %{name}+cgdisplaystream
This metapackage enables feature "CGDisplayStream" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cgexrtonemappinggamma
Summary:        Bindings to the CoreGraphics framework - feature "CGEXRToneMappingGamma" and 3 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Provides:       crate(%{pkgname}/cgexrtonemappinggamma)
Provides:       crate(%{pkgname}/cgpsconverter)
Provides:       crate(%{pkgname}/cgsession)
Provides:       crate(%{pkgname}/cgtonemapping)

%description -n %{name}+cgexrtonemappinggamma
This metapackage enables feature "CGEXRToneMappingGamma" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CGPSConverter", "CGSession", and "CGToneMapping" features.

%package     -n %{name}+cgevent
Summary:        Bindings to the CoreGraphics framework - feature "CGEvent"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdata) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfmachport) >= 0.3.2
Provides:       crate(%{pkgname}/cgevent)

%description -n %{name}+cgevent
This metapackage enables feature "CGEvent" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cgeventsource
Summary:        Bindings to the CoreGraphics framework - feature "CGEventSource" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-core-foundation-0.3/cfdate) >= 0.3.2
Provides:       crate(%{pkgname}/cgeventsource)
Provides:       crate(%{pkgname}/cgpdfstring)

%description -n %{name}+cgeventsource
This metapackage enables feature "CGEventSource" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CGPDFString" feature.

%package     -n %{name}+cgfont
Summary:        Bindings to the CoreGraphics framework - feature "CGFont"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-core-foundation-0.3/cfarray) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdata) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Provides:       crate(%{pkgname}/cgfont)

%description -n %{name}+cgfont
This metapackage enables feature "CGFont" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cggradient
Summary:        Bindings to the CoreGraphics framework - feature "CGGradient" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-core-foundation-0.3/cfarray) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Provides:       crate(%{pkgname}/cggradient)
Provides:       crate(%{pkgname}/cgwindow)

%description -n %{name}+cggradient
This metapackage enables feature "CGGradient" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CGWindow" feature.

%package     -n %{name}+cgimage
Summary:        Bindings to the CoreGraphics framework - feature "CGImage"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Provides:       crate(%{pkgname}/cgimage)

%description -n %{name}+cgimage
This metapackage enables feature "CGImage" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cgpdfcontentstream
Summary:        Bindings to the CoreGraphics framework - feature "CGPDFContentStream"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-core-foundation-0.3/cfarray) >= 0.3.2
Provides:       crate(%{pkgname}/cgpdfcontentstream)

%description -n %{name}+cgpdfcontentstream
This metapackage enables feature "CGPDFContentStream" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cgpdfcontext
Summary:        Bindings to the CoreGraphics framework - feature "CGPDFContext"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdata) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfurl) >= 0.3.2
Provides:       crate(%{pkgname}/cgpdfcontext)

%description -n %{name}+cgpdfcontext
This metapackage enables feature "CGPDFContext" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cgpdfdocument
Summary:        Bindings to the CoreGraphics framework - feature "CGPDFDocument"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfurl) >= 0.3.2
Provides:       crate(%{pkgname}/cgpdfdocument)

%description -n %{name}+cgpdfdocument
This metapackage enables feature "CGPDFDocument" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cgpdfstream
Summary:        Bindings to the CoreGraphics framework - feature "CGPDFStream" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-core-foundation-0.3/cfdata) >= 0.3.2
Provides:       crate(%{pkgname}/cgpdfstream)
Provides:       crate(%{pkgname}/cgrenderingbufferprovider)

%description -n %{name}+cgpdfstream
This metapackage enables feature "CGPDFStream" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CGRenderingBufferProvider" feature.

%package     -n %{name}+cgpath
Summary:        Bindings to the CoreGraphics framework - feature "CGPath"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-core-foundation-0.3/cfarray) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Provides:       crate(%{pkgname}/cgpath)

%description -n %{name}+cgpath
This metapackage enables feature "CGPath" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cgremoteoperation
Summary:        Bindings to the CoreGraphics framework - feature "CGRemoteOperation"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdate) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfmachport) >= 0.3.2
Provides:       crate(%{pkgname}/cgremoteoperation)

%description -n %{name}+cgremoteoperation
This metapackage enables feature "CGRemoteOperation" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bitflags
Summary:        Bindings to the CoreGraphics framework - feature "bitflags" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(bitflags-2.0/std) >= 2.11.0
Provides:       crate(%{pkgname}/bitflags)
Provides:       crate(%{pkgname}/cgeventtypes)

%description -n %{name}+bitflags
This metapackage enables feature "bitflags" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CGEventTypes" feature.

%package     -n %{name}+block2
Summary:        Bindings to the CoreGraphics framework - feature "block2"
Requires:       crate(%{pkgname})
Requires:       crate(block2-0.6/alloc) >= 0.6.1
Provides:       crate(%{pkgname}/block2)

%description -n %{name}+block2
This metapackage enables feature "block2" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Bindings to the CoreGraphics framework - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(%{pkgname}/block2)
Requires:       crate(%{pkgname}/cgaffinetransform)
Requires:       crate(%{pkgname}/cgbase)
Requires:       crate(%{pkgname}/cgbitmapcontext)
Requires:       crate(%{pkgname}/cgcolor)
Requires:       crate(%{pkgname}/cgcolorconversioninfo)
Requires:       crate(%{pkgname}/cgcolorspace)
Requires:       crate(%{pkgname}/cgcontext)
Requires:       crate(%{pkgname}/cgconvertcolordatawithformat)
Requires:       crate(%{pkgname}/cgdataconsumer)
Requires:       crate(%{pkgname}/cgdataprovider)
Requires:       crate(%{pkgname}/cgdirectdisplay)
Requires:       crate(%{pkgname}/cgdirectdisplaymetal)
Requires:       crate(%{pkgname}/cgdirectpalette)
Requires:       crate(%{pkgname}/cgdisplayconfiguration)
Requires:       crate(%{pkgname}/cgdisplayfade)
Requires:       crate(%{pkgname}/cgdisplaystream)
Requires:       crate(%{pkgname}/cgerror)
Requires:       crate(%{pkgname}/cgevent)
Requires:       crate(%{pkgname}/cgeventsource)
Requires:       crate(%{pkgname}/cgeventtypes)
Requires:       crate(%{pkgname}/cgexrtonemappinggamma)
Requires:       crate(%{pkgname}/cgfont)
Requires:       crate(%{pkgname}/cgfunction)
Requires:       crate(%{pkgname}/cggeometry)
Requires:       crate(%{pkgname}/cggradient)
Requires:       crate(%{pkgname}/cgimage)
Requires:       crate(%{pkgname}/cgitutonemapping)
Requires:       crate(%{pkgname}/cglayer)
Requires:       crate(%{pkgname}/cgpath)
Requires:       crate(%{pkgname}/cgpattern)
Requires:       crate(%{pkgname}/cgpdfarray)
Requires:       crate(%{pkgname}/cgpdfcontentstream)
Requires:       crate(%{pkgname}/cgpdfcontext)
Requires:       crate(%{pkgname}/cgpdfdictionary)
Requires:       crate(%{pkgname}/cgpdfdocument)
Requires:       crate(%{pkgname}/cgpdfobject)
Requires:       crate(%{pkgname}/cgpdfoperatortable)
Requires:       crate(%{pkgname}/cgpdfpage)
Requires:       crate(%{pkgname}/cgpdfscanner)
Requires:       crate(%{pkgname}/cgpdfstream)
Requires:       crate(%{pkgname}/cgpdfstring)
Requires:       crate(%{pkgname}/cgpsconverter)
Requires:       crate(%{pkgname}/cgremoteoperation)
Requires:       crate(%{pkgname}/cgrenderingbufferprovider)
Requires:       crate(%{pkgname}/cgsession)
Requires:       crate(%{pkgname}/cgshading)
Requires:       crate(%{pkgname}/cgtonemapping)
Requires:       crate(%{pkgname}/cgwindow)
Requires:       crate(%{pkgname}/cgwindowlevel)
Requires:       crate(%{pkgname}/dispatch2)
Requires:       crate(%{pkgname}/libc)
Requires:       crate(%{pkgname}/objc2)
Requires:       crate(%{pkgname}/objc2-metal)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dispatch2
Summary:        Bindings to the CoreGraphics framework - feature "dispatch2"
Requires:       crate(%{pkgname})
Requires:       crate(dispatch2-0.3/alloc) >= 0.3.1
Provides:       crate(%{pkgname}/dispatch2)

%description -n %{name}+dispatch2
This metapackage enables feature "dispatch2" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libc
Summary:        Bindings to the CoreGraphics framework - feature "libc"
Requires:       crate(%{pkgname})
Requires:       crate(libc-0.2) >= 0.2.80
Provides:       crate(%{pkgname}/libc)

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2
Summary:        Bindings to the CoreGraphics framework - feature "objc2"
Requires:       crate(%{pkgname})
Requires:       crate(dispatch2-0.3/alloc) >= 0.3.1
Requires:       crate(dispatch2-0.3/objc2) >= 0.3.1
Requires:       crate(objc2-0.6/std) >= 0.6.4
Requires:       crate(objc2-core-foundation-0.3/objc2) >= 0.3.2
Requires:       crate(objc2-io-surface-0.3/iosurfaceref) >= 0.3.2
Requires:       crate(objc2-io-surface-0.3/objc2) >= 0.3.2
Provides:       crate(%{pkgname}/objc2)

%description -n %{name}+objc2
This metapackage enables feature "objc2" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-io-surface
Summary:        Bindings to the CoreGraphics framework - feature "objc2-io-surface"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-io-surface-0.3/iosurfaceref) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-io-surface)

%description -n %{name}+objc2-io-surface
This metapackage enables feature "objc2-io-surface" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-metal
Summary:        Bindings to the CoreGraphics framework - feature "objc2-metal"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-metal-0.3/mtldevice) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-metal)

%description -n %{name}+objc2-metal
This metapackage enables feature "objc2-metal" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
