# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
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
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(objc2-core-foundation-0.3) >= 0.3.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/ctdefines) = %{version}
Provides:       crate(%{pkgname}/ctfontmanagererrors) = %{version}
Provides:       crate(%{pkgname}/ctglyphinfo) = %{version}
Provides:       crate(%{pkgname}/ctparagraphstyle) = %{version}
Provides:       crate(%{pkgname}/sfntlayouttypes) = %{version}
Provides:       crate(%{pkgname}/sfnttypes) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/unstable-darwin-objc) = %{version}

%description
Source code for takopackized Rust crate "objc2-core-text"

%package     -n %{name}+ctfont
Summary:        Bindings to the CoreText framework - feature "CTFont"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfarray) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfcharacterset) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdata) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfstring) >= 0.3.2
Provides:       crate(%{pkgname}/ctfont) = %{version}

%description -n %{name}+ctfont
This metapackage enables feature "CTFont" for the Rust objc2-core-text crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ctfontcollection
Summary:        Bindings to the CoreText framework - feature "CTFontCollection"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfarray) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfset) >= 0.3.2
Provides:       crate(%{pkgname}/ctfontcollection) = %{version}

%description -n %{name}+ctfontcollection
This metapackage enables feature "CTFontCollection" for the Rust objc2-core-text crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ctfontdescriptor
Summary:        Bindings to the CoreText framework - feature "CTFontDescriptor"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfarray) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfnumber) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfset) >= 0.3.2
Provides:       crate(%{pkgname}/ctfontdescriptor) = %{version}

%description -n %{name}+ctfontdescriptor
This metapackage enables feature "CTFontDescriptor" for the Rust objc2-core-text crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ctfontmanager
Summary:        Bindings to the CoreText framework - feature "CTFontManager"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfarray) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfbundle) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdata) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cferror) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfrunloop) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfurl) >= 0.3.2
Provides:       crate(%{pkgname}/ctfontmanager) = %{version}

%description -n %{name}+ctfontmanager
This metapackage enables feature "CTFontManager" for the Rust objc2-core-text crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ctframe
Summary:        Bindings to the CoreText framework - feature "CTFrame"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfarray) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Provides:       crate(%{pkgname}/ctframe) = %{version}

%description -n %{name}+ctframe
This metapackage enables feature "CTFrame" for the Rust objc2-core-text crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ctframesetter
Summary:        Bindings to the CoreText framework - feature "CTFramesetter"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfattributedstring) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Provides:       crate(%{pkgname}/ctframesetter) = %{version}

%description -n %{name}+ctframesetter
This metapackage enables feature "CTFramesetter" for the Rust objc2-core-text crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ctline
Summary:        Bindings to the CoreText framework - feature "CTLine"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfarray) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfattributedstring) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Provides:       crate(%{pkgname}/ctline) = %{version}

%description -n %{name}+ctline
This metapackage enables feature "CTLine" for the Rust objc2-core-text crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ctrubyannotation
Summary:        Bindings to the CoreText framework - feature "CTRubyAnnotation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Provides:       crate(%{pkgname}/ctrubyannotation) = %{version}

%description -n %{name}+ctrubyannotation
This metapackage enables feature "CTRubyAnnotation" for the Rust objc2-core-text crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ctrun
Summary:        Bindings to the CoreText framework - feature "CTRun"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Provides:       crate(%{pkgname}/ctrun) = %{version}

%description -n %{name}+ctrun
This metapackage enables feature "CTRun" for the Rust objc2-core-text crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ctrundelegate
Summary:        Bindings to the CoreText framework - feature "CTRunDelegate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Provides:       crate(%{pkgname}/ctrundelegate) = %{version}

%description -n %{name}+ctrundelegate
This metapackage enables feature "CTRunDelegate" for the Rust objc2-core-text crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cttexttab
Summary:        Bindings to the CoreText framework - feature "CTTextTab"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Provides:       crate(%{pkgname}/cttexttab) = %{version}

%description -n %{name}+cttexttab
This metapackage enables feature "CTTextTab" for the Rust objc2-core-text crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cttypesetter
Summary:        Bindings to the CoreText framework - feature "CTTypesetter"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfattributedstring) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Provides:       crate(%{pkgname}/cttypesetter) = %{version}

%description -n %{name}+cttypesetter
This metapackage enables feature "CTTypesetter" for the Rust objc2-core-text crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bitflags
Summary:        Bindings to the CoreText framework - feature "bitflags" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bitflags-2/std) >= 2.5.0
Provides:       crate(%{pkgname}/bitflags) = %{version}
Provides:       crate(%{pkgname}/ctfonttraits) = %{version}
Provides:       crate(%{pkgname}/ctstringattributes) = %{version}

%description -n %{name}+bitflags
This metapackage enables feature "bitflags" for the Rust objc2-core-text crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CTFontTraits", and "CTStringAttributes" features.

%package     -n %{name}+block2
Summary:        Bindings to the CoreText framework - feature "block2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block2-0.6/alloc) >= 0.6.1
Provides:       crate(%{pkgname}/block2) = %{version}

%description -n %{name}+block2
This metapackage enables feature "block2" for the Rust objc2-core-text crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Bindings to the CoreText framework - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(%{pkgname}/block2) = %{version}
Requires:       crate(%{pkgname}/ctdefines) = %{version}
Requires:       crate(%{pkgname}/ctfont) = %{version}
Requires:       crate(%{pkgname}/ctfontcollection) = %{version}
Requires:       crate(%{pkgname}/ctfontdescriptor) = %{version}
Requires:       crate(%{pkgname}/ctfontmanager) = %{version}
Requires:       crate(%{pkgname}/ctfontmanagererrors) = %{version}
Requires:       crate(%{pkgname}/ctfonttraits) = %{version}
Requires:       crate(%{pkgname}/ctframe) = %{version}
Requires:       crate(%{pkgname}/ctframesetter) = %{version}
Requires:       crate(%{pkgname}/ctglyphinfo) = %{version}
Requires:       crate(%{pkgname}/ctline) = %{version}
Requires:       crate(%{pkgname}/ctparagraphstyle) = %{version}
Requires:       crate(%{pkgname}/ctrubyannotation) = %{version}
Requires:       crate(%{pkgname}/ctrun) = %{version}
Requires:       crate(%{pkgname}/ctrundelegate) = %{version}
Requires:       crate(%{pkgname}/ctstringattributes) = %{version}
Requires:       crate(%{pkgname}/cttexttab) = %{version}
Requires:       crate(%{pkgname}/cttypesetter) = %{version}
Requires:       crate(%{pkgname}/libc) = %{version}
Requires:       crate(%{pkgname}/objc2) = %{version}
Requires:       crate(%{pkgname}/objc2-core-graphics) = %{version}
Requires:       crate(%{pkgname}/sfntlayouttypes) = %{version}
Requires:       crate(%{pkgname}/sfnttypes) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust objc2-core-text crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libc
Summary:        Bindings to the CoreText framework - feature "libc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2) >= 0.2.80
Provides:       crate(%{pkgname}/libc) = %{version}

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust objc2-core-text crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2
Summary:        Bindings to the CoreText framework - feature "objc2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-0.6/std) >= 0.6.2
Requires:       crate(objc2-core-foundation-0.3/objc2) >= 0.3.2
Requires:       crate(objc2-core-graphics-0.3/cgcontext) >= 0.3.2
Requires:       crate(objc2-core-graphics-0.3/cgfont) >= 0.3.2
Requires:       crate(objc2-core-graphics-0.3/cgimage) >= 0.3.2
Requires:       crate(objc2-core-graphics-0.3/cgpath) >= 0.3.2
Requires:       crate(objc2-core-graphics-0.3/objc2) >= 0.3.2
Provides:       crate(%{pkgname}/objc2) = %{version}

%description -n %{name}+objc2
This metapackage enables feature "objc2" for the Rust objc2-core-text crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-core-graphics
Summary:        Bindings to the CoreText framework - feature "objc2-core-graphics"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-graphics-0.3/cgcontext) >= 0.3.2
Requires:       crate(objc2-core-graphics-0.3/cgfont) >= 0.3.2
Requires:       crate(objc2-core-graphics-0.3/cgimage) >= 0.3.2
Requires:       crate(objc2-core-graphics-0.3/cgpath) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-core-graphics) = %{version}

%description -n %{name}+objc2-core-graphics
This metapackage enables feature "objc2-core-graphics" for the Rust objc2-core-text crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
