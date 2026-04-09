# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# skip test as we don't have fonts to test
%bcond tests 0

Name:           fcft
Version:        3.3.3
Release:        %autorelease
Summary:        Simple library for font loading and glyph rasterization
License:        MIT AND Unicode-3.0 AND Zlib
URL:            https://codeberg.org/dnkl/fcft
#!RemoteAsset:  sha256:bb298772d625e7d917373d541456f34f1957a9e22b16f17f64158b2c3816563c
Source0:        https://codeberg.org/dnkl/fcft/releases/download/%{version}/fcft-%{version}.tar.gz
BuildSystem:    meson

%if %{with tests}
BuildOption(conf):  -Dtest-text-shaping=true
%else
BuildOption(conf):  -Dtest-text-shaping=false
%endif
BuildOption(conf):  -Ddocs=enabled

BuildRequires:  meson >= 0.58.0
BuildRequires:  gcc
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(libutf8proc)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(tllist)
BuildRequires:  pkgconfig(scdoc)
%if %{with tests}
BuildRequires:  pkgconfig(check)
BuildRequires:  font(dejavuserif)
BuildRequires:  font(notoemoji)
%endif

Provides:       bundled(nanosvg)

%description
fcft is a small font loading and glyph rasterization library built
on top of FontConfig, FreeType2 and pixman.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep -a
cp 3rd-party/nanosvg/LICENSE.txt LICENSE.nanosvg
cp unicode/license.txt LICENSE.Unicode

%install -a
rm -f %{buildroot}%{_docdir}/%{name}/LICENSE

%if %{without tests}
%check
%endif

%files
%license LICENSE LICENSE.nanosvg LICENSE.Unicode
%doc %{_docdir}/fcft/README.md
%doc %{_docdir}/fcft/CHANGELOG.md
%{_libdir}/libfcft.so.*

%files devel
%{_includedir}/fcft/
%{_libdir}/libfcft.so
%{_libdir}/pkgconfig/fcft.pc
%{_mandir}/man3/

%changelog
%autochangelog
