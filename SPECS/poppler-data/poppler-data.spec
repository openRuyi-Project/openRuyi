# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define ver 0_4_12

Name:           poppler-data
Version:        0.4.12
Release:        %autorelease
Summary:        Encoding Files for use with poppler
License:        BSD-3-Clause AND GPL-2.0-only AND GPL-3.0-only
URL:            https://poppler.freedesktop.org/
VCS:            git:https://gitlab.freedesktop.org/poppler/poppler-data
#!RemoteAsset
Source:         https://gitlab.freedesktop.org/poppler/poppler-data/-/archive/POPPLER_DATA_%{ver}/poppler-data-POPPLER_DATA_%{ver}.tar.gz
BuildSystem:    autotools

BuildOption(install):  prefix=%{_prefix}

BuildRequires:  make

%description
This package consists of encoding files for use with poppler. The
encoding files are optional and poppler will automatically read them if
they are present. When installed, the encoding files enable poppler
to correctly render CJK and Cyrillic text properly.

%package        devel
Summary:        Developer files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
This package contains the pkgconfig file for %{name}, which is useful
for detecting the installation of poppler-data.

# No configure.
%conf

# No tests.
%check

%files
%license COPYING*
%doc README
%{_datadir}/poppler/

%files devel
%{_datadir}/pkgconfig/poppler-data.pc

%changelog
%autochangelog
