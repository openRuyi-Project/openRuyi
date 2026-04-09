# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           hdparm
Version:        9.65
Release:        %autorelease
Summary:        A utility for displaying and/or setting hard disk parameters
License:        hdparm
URL:            https://sourceforge.net/projects/hdparm/
#!RemoteAsset
Source:         https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(install):  sbindir=%{_sbindir}

BuildRequires:  make

%description
Hdparm is a useful system utility for setting (E)IDE hard drive
parameters.  For example, hdparm can be used to tweak hard drive
performance and to spin down hard drives for power conservation.

%conf
# No configure

# No test suite
%check

%install -p
mkdir -p "%{buildroot}%{_mandir}/man8"

%files
%doc hdparm.lsm Changelog README.acoustic TODO
%license LICENSE.TXT
%{_sbindir}/hdparm
%{_mandir}/man8/hdparm.8*

%changelog
%autochangelog
