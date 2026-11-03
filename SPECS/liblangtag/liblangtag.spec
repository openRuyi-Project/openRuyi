# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           liblangtag
Version:        0.6.8
Release:        %autorelease
Summary:        BCP 47 language tag parsing and matching library
License:        (LGPL-3.0-or-later OR MPL-2.0) AND Unicode-DFS-2016
URL:            https://github.com/tagoh/liblangtag
#!RemoteAsset:  sha256:a96975b79ddd8fef6d9295c083fe3f1afa1a8898a57235d4069255ade44e5cf2
Source0:        https://gitlab.com/tagoh/liblangtag/-/releases/%{version}/downloads/%{name}-%{version}.tar.bz2
#!RemoteAsset:  sha256:10223cc8c219427c86a4c66ce98282a00c7f4d9b0609355146282344783007f2
Source1:        https://dev-www.libreoffice.org/src/language-subtag-registry-2026-9-17.tar.bz2
#!RemoteAsset:  sha256:e6795346adb86b0fcd0df1fdeadbdbbf5276520e85fdf3d268a1196b532131ba
Source2:        https://raw.githubusercontent.com/unicode-org/cldr/1e28c0fbb43b719b43127432f0a86323578789a4/unicode-license.txt
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-introspection
BuildOption(conf):  --enable-test
BuildOption(conf):  --enable-rebuild-data

BuildRequires:  glibc-locale-base
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(check) >= 0.11.0
BuildRequires:  pkgconfig(libxml-2.0) >= 2.1.0

%description
liblangtag parses, canonicalizes and compares BCP 47 language tags.
It uses the IANA language subtag registry and Unicode CLDR data to
resolve language, region, script and extension subtags.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and pkg-config metadata for using liblangtag.

%prep -a
tar -xf %{SOURCE1} data/language-subtag-registry
rm -f data/language-subtag-registry.xml
cp -p %{SOURCE2} Unicode-LICENSE.txt

%check -a
# Verify the generated language-subtag registry has the date of the IANA data used by this release.
grep -F '<registry date="2026-09-17">' data/language-subtag-registry.xml

%files
%doc AUTHORS README
%license COPYING Unicode-LICENSE.txt
%{_datadir}/liblangtag/
%{_libdir}/liblangtag/
%{_libdir}/liblangtag.so.*

%files devel
%doc %{_datadir}/gtk-doc/html/liblangtag/
%{_includedir}/liblangtag/
%{_libdir}/liblangtag.so
%{_libdir}/pkgconfig/liblangtag.pc

%changelog
%autochangelog
