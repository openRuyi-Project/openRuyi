# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name objc2-core-text
%global full_version 0.3.2
%global pkgname objc2-core-text-0.3

Name:           rust-objc2-core-text-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "objc2-core-text"
License:        Zlib OR Apache-2.0 OR MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:0cde0dfb48d25d2b4862161a4d5fcc0e3c24367869ad306b0c9ec0073bfed92d
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(objc2-core-foundation-0.3) >= 0.3.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/ctdefines)
Provides:       crate(%{pkgname}/ctfontmanagererrors)
Provides:       crate(%{pkgname}/ctglyphinfo)
Provides:       crate(%{pkgname}/ctparagraphstyle)
Provides:       crate(%{pkgname}/sfntlayouttypes)
Provides:       crate(%{pkgname}/sfnttypes)
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/unstable-darwin-objc)

%description
Source code for takopackized Rust crate "objc2-core-text"

%package     -n %{name}+ctfont
Summary:        Bindings to the CoreText framework - feature "CTFont"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-core-foundation-0.3/cfarray) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfcharacterset) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdata) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfstring) >= 0.3.2
Provides:       crate(%{pkgname}/ctfont)

%description -n %{name}+ctfont
This metapackage enables feature "CTFont" for the Rust objc2-core-text crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ctfontcollection
Summary:        Bindings to the CoreText framework - feature "CTFontCollection"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-core-foundation-0.3/cfarray) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfset) >= 0.3.2
Provides:       crate(%{pkgname}/ctfontcollection)

%description -n %{name}+ctfontcollection
This metapackage enables feature "CTFontCollection" for the Rust objc2-core-text crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ctfontdescriptor
Summary:        Bindings to the CoreText framework - feature "CTFontDescriptor"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-core-foundation-0.3/cfarray) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfnumber) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfset) >= 0.3.2
Provides:       crate(%{pkgname}/ctfontdescriptor)

%description -n %{name}+ctfontdescriptor
This metapackage enables feature "CTFontDescriptor" for the Rust objc2-core-text crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ctfontmanager
Summary:        Bindings to the CoreText framework - feature "CTFontManager"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-core-foundation-0.3/cfarray) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfbundle) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdata) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cferror) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfrunloop) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfurl) >= 0.3.2
Provides:       crate(%{pkgname}/ctfontmanager)

%description -n %{name}+ctfontmanager
This metapackage enables feature "CTFontManager" for the Rust objc2-core-text crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ctframe
Summary:        Bindings to the CoreText framework - feature "CTFrame"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-core-foundation-0.3/cfarray) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Provides:       crate(%{pkgname}/ctframe)

%description -n %{name}+ctframe
This metapackage enables feature "CTFrame" for the Rust objc2-core-text crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ctframesetter
Summary:        Bindings to the CoreText framework - feature "CTFramesetter"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-core-foundation-0.3/cfattributedstring) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Provides:       crate(%{pkgname}/ctframesetter)

%description -n %{name}+ctframesetter
This metapackage enables feature "CTFramesetter" for the Rust objc2-core-text crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ctline
Summary:        Bindings to the CoreText framework - feature "CTLine"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-core-foundation-0.3/cfarray) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfattributedstring) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Provides:       crate(%{pkgname}/ctline)

%description -n %{name}+ctline
This metapackage enables feature "CTLine" for the Rust objc2-core-text crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ctrubyannotation
Summary:        Bindings to the CoreText framework - feature "CTRubyAnnotation"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Provides:       crate(%{pkgname}/ctrubyannotation)

%description -n %{name}+ctrubyannotation
This metapackage enables feature "CTRubyAnnotation" for the Rust objc2-core-text crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ctrun
Summary:        Bindings to the CoreText framework - feature "CTRun"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Provides:       crate(%{pkgname}/ctrun)

%description -n %{name}+ctrun
This metapackage enables feature "CTRun" for the Rust objc2-core-text crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ctrundelegate
Summary:        Bindings to the CoreText framework - feature "CTRunDelegate"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Provides:       crate(%{pkgname}/ctrundelegate)

%description -n %{name}+ctrundelegate
This metapackage enables feature "CTRunDelegate" for the Rust objc2-core-text crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cttexttab
Summary:        Bindings to the CoreText framework - feature "CTTextTab"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Provides:       crate(%{pkgname}/cttexttab)

%description -n %{name}+cttexttab
This metapackage enables feature "CTTextTab" for the Rust objc2-core-text crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cttypesetter
Summary:        Bindings to the CoreText framework - feature "CTTypesetter"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-core-foundation-0.3/cfattributedstring) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Provides:       crate(%{pkgname}/cttypesetter)

%description -n %{name}+cttypesetter
This metapackage enables feature "CTTypesetter" for the Rust objc2-core-text crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bitflags
Summary:        Bindings to the CoreText framework - feature "bitflags" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(bitflags-2.0/std) >= 2.11.0
Provides:       crate(%{pkgname}/bitflags)
Provides:       crate(%{pkgname}/ctfonttraits)
Provides:       crate(%{pkgname}/ctstringattributes)

%description -n %{name}+bitflags
This metapackage enables feature "bitflags" for the Rust objc2-core-text crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CTFontTraits", and "CTStringAttributes" features.

%package     -n %{name}+block2
Summary:        Bindings to the CoreText framework - feature "block2"
Requires:       crate(%{pkgname})
Requires:       crate(block2-0.6/alloc) >= 0.6.1
Provides:       crate(%{pkgname}/block2)

%description -n %{name}+block2
This metapackage enables feature "block2" for the Rust objc2-core-text crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Bindings to the CoreText framework - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(%{pkgname}/block2)
Requires:       crate(%{pkgname}/ctdefines)
Requires:       crate(%{pkgname}/ctfont)
Requires:       crate(%{pkgname}/ctfontcollection)
Requires:       crate(%{pkgname}/ctfontdescriptor)
Requires:       crate(%{pkgname}/ctfontmanager)
Requires:       crate(%{pkgname}/ctfontmanagererrors)
Requires:       crate(%{pkgname}/ctfonttraits)
Requires:       crate(%{pkgname}/ctframe)
Requires:       crate(%{pkgname}/ctframesetter)
Requires:       crate(%{pkgname}/ctglyphinfo)
Requires:       crate(%{pkgname}/ctline)
Requires:       crate(%{pkgname}/ctparagraphstyle)
Requires:       crate(%{pkgname}/ctrubyannotation)
Requires:       crate(%{pkgname}/ctrun)
Requires:       crate(%{pkgname}/ctrundelegate)
Requires:       crate(%{pkgname}/ctstringattributes)
Requires:       crate(%{pkgname}/cttexttab)
Requires:       crate(%{pkgname}/cttypesetter)
Requires:       crate(%{pkgname}/libc)
Requires:       crate(%{pkgname}/objc2)
Requires:       crate(%{pkgname}/objc2-core-graphics)
Requires:       crate(%{pkgname}/sfntlayouttypes)
Requires:       crate(%{pkgname}/sfnttypes)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust objc2-core-text crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libc
Summary:        Bindings to the CoreText framework - feature "libc"
Requires:       crate(%{pkgname})
Requires:       crate(libc-0.2) >= 0.2.80
Provides:       crate(%{pkgname}/libc)

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust objc2-core-text crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2
Summary:        Bindings to the CoreText framework - feature "objc2"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-0.6/std) >= 0.6.4
Requires:       crate(objc2-core-foundation-0.3/objc2) >= 0.3.2
Requires:       crate(objc2-core-graphics-0.3/cgcontext) >= 0.3.2
Requires:       crate(objc2-core-graphics-0.3/cgfont) >= 0.3.2
Requires:       crate(objc2-core-graphics-0.3/cgimage) >= 0.3.2
Requires:       crate(objc2-core-graphics-0.3/cgpath) >= 0.3.2
Requires:       crate(objc2-core-graphics-0.3/objc2) >= 0.3.2
Provides:       crate(%{pkgname}/objc2)

%description -n %{name}+objc2
This metapackage enables feature "objc2" for the Rust objc2-core-text crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-core-graphics
Summary:        Bindings to the CoreText framework - feature "objc2-core-graphics"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-core-graphics-0.3/cgcontext) >= 0.3.2
Requires:       crate(objc2-core-graphics-0.3/cgfont) >= 0.3.2
Requires:       crate(objc2-core-graphics-0.3/cgimage) >= 0.3.2
Requires:       crate(objc2-core-graphics-0.3/cgpath) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-core-graphics)

%description -n %{name}+objc2-core-graphics
This metapackage enables feature "objc2-core-graphics" for the Rust objc2-core-text crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
