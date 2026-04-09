# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define d_version 3-6

Name:           dmidecode
Version:        3.6
Release:        %autorelease
Summary:        DMI data report tool
License:        GPL-2.0-or-later
URL:            https://www.nongnu.org/dmidecode/
VCS:            git:https://git.savannah.nongnu.org/git/dmidecode.git
#!RemoteAsset
Source:         https://github.com/mirror/dmidecode/archive/refs/tags/%{name}-%{d_version}.tar.gz
BuildSystem:    autotools

BuildOption(build):  CFLAGS="%{optflags}"
BuildOption(build):  LDFLAGS="%{?build_ldflags}"
BuildOption(install):  prefix=%{_prefix}
BuildOption(install):  sbindir=%{_sbindir}

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  xz

%description
Dmidecode reports information about your system's hardware as described
in your system BIOS according to the SMBIOS/DMI standard. This information
typically includes system manufacturer, model name, serial number, BIOS
version, and asset tag.

# No configure
%conf

# No `check' target.
%check

%files
%{_docdir}/%{name}
%{_sbindir}/*
%{_mandir}/man8/*.8*

%changelog
%autochangelog
