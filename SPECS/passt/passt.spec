# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit f758d93125e5980996348a11486af507b3912fcb

Name:           passt
Version:        0+git20260328.f758d93
Release:        %autorelease
Summary:        Plug A Simple Socket Transport
License:        GPL-2.0-or-later AND BSD-3-Clause
URL:            https://passt.top/passt
#!RemoteAsset:  sha256:464e87722a58764b59e0612ba1b7c311e2248b505da3146b5e33d19a292f8aa1
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
%license LICENSES/{GPL-2.0-or-later.txt,BSD-3-Clause.txt}
%doc README.md doc/demo.sh
%{_mandir}/man1/passt*
%{_mandir}/man1/pasta*
%{_mandir}/man1/qrap.1*
%{_bindir}/passt*
%{_bindir}/pasta*
%{_bindir}/qrap

%changelog
%autochangelog
