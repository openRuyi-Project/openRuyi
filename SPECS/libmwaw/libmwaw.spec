# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libmwaw
Version:        0.3.23
Release:        %autorelease
Summary:        Classic Macintosh document import library
License:        (MPL-2.0 OR LGPL-2.0-or-later) AND LGPL-2.1-or-later AND LicenseRef-X0213
URL:            https://sourceforge.net/projects/libmwaw/
VCS:            git:https://git.code.sf.net/p/libmwaw/libmwaw
#!RemoteAsset:  sha256:ac3590f691a2904eb8c7dc8b757b8a29f125f592449e421459ae8fa928b399eb
Source0:        https://downloads.sourceforge.net/libmwaw/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --enable-tools
BuildOption(conf):  --without-docs

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(librevenge-generators-0.0)
BuildRequires:  pkgconfig(librevenge-stream-0.0)
BuildRequires:  pkgconfig(zlib)

%description
libmwaw reads legacy Macintosh text, spreadsheet, drawing and
presentation documents. Its conversion tools export text, HTML, CSV and SVG.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and pkg-config metadata for developing with %{name}.

%prep -a
sed -n '/^## License:/,/^## Note:/{ /^## Note:/d; s/^##[[:space:]]*//; p; }' src/lib/MWAWFontSJISConverter.cxx > X0213-LICENSE.txt
grep -F 'distribute this table freely' X0213-LICENSE.txt

%files
%doc README
%license COPYING.MPL COPYING.LGPL X0213-LICENSE.txt
%{_bindir}/mwaw2csv
%{_bindir}/mwaw2html
%{_bindir}/mwaw2raw
%{_bindir}/mwaw2svg
%{_bindir}/mwaw2text
%{_bindir}/mwawFile
%{_bindir}/mwawZip
%{_libdir}/libmwaw-0.3.so.*

%files devel
%{_includedir}/libmwaw-0.3/
%{_libdir}/libmwaw-0.3.so
%{_libdir}/pkgconfig/libmwaw-0.3.pc

%changelog
%autochangelog
