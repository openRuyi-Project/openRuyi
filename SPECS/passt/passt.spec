# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit ec96f0124282338cd2b2e65ff1aa3def8882ae23

Name:           passt
Version:        0+git20260424.ec96f01
Release:        %autorelease
Summary:        Plug A Simple Socket Transport
License:        GPL-2.0-or-later AND BSD-3-Clause
URL:            https://passt.top/passt
#!RemoteAsset:  sha256:416094ef9ad15ab5696e9988c8f06c0e2954ed847abbcb2004d12e1491409bb2
Source:         https://passt.top/passt/snapshot/passt-%{commit}.tar.xz
BuildSystem:    autotools

BuildOption(prep):  -p1 -n %{name}-%{commit}
BuildOption(build):  VERSION=%{version}
BuildOption(install):  DESTDIR=%{buildroot}
BuildOption(install):  prefix=%{_prefix}

BuildRequires:  make

%description
Plug A Simple Socket Transport.

# No configure.
%conf

# No tests.
%check

%files
%doc README.md doc/demo.sh
%license LICENSES/GPL-2.0-or-later.txt
%license LICENSES/BSD-3-Clause.txt
%{_mandir}/man1/passt*
%{_mandir}/man1/pasta*
%{_mandir}/man1/qrap.1*
%{_bindir}/passt*
%{_bindir}/pasta*
%{_bindir}/qrap

%changelog
%autochangelog
