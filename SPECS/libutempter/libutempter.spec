# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libutempter
Version:        1.2.3
Release:        %autorelease
Summary:        A privileged helper for utmp/wtmp updates
License:        LGPL-2.1-or-later
URL:            https://github.com/altlinux/libutempter
#!RemoteAsset
Source:         https://github.com/altlinux/libutempter/archive/refs/tags/%{version}-alt1.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    autotools

Patch0:         0001-fix-install-path.patch

BuildOption(build):  -C libutempter libdir=%{_libdir} libexecdir=%{_libexecdir}
BuildOption(install):  -C libutempter libdir=%{_libdir} libexecdir=%{_libexecdir}

BuildRequires:  gcc

Requires(pre):  shadow

%description
This library supports saving session records to utmp and wtmp
files.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.

# No configure
%conf

# No tests.
%check

%files
%{_libdir}/libutempter.so.*
%{_libexecdir}/utempter/utempter
%{_mandir}/man3/*

%files devel
%{_includedir}/utempter.h
%{_libdir}/libutempter.so

%changelog
%autochangelog
