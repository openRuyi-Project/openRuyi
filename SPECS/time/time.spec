# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Icenowy Zheng <zhengxingda@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global optflags %optflags -Wno-error=incompatible-pointer-types

Name:           time
Version:        1.10
Release:        %autorelease
Summary:        Run Programs And Summarize System Resource Usage
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/time/
VCS:            git:https://https.git.savannah.gnu.org/git/time.git
#!RemoteAsset:  sha256:e8c29fb4ab599d8478e41e8618f50db8aede9c90af27d0d2ef28ae50d5de09c3
Source:         https://ftpmirror.gnu.org/gnu/time/%{name}-%{version}.tar.gz
BuildSystem:    autotools

%description
The "time" command runs another program, then displays information
about the resources used by that program, collected by the system
while the program was running.

%install -a
install -d %{buildroot}%{_mandir}/man1

%files
%license COPYING
%doc AUTHORS NEWS README
%{_bindir}/time
%{_infodir}/time.info*

%changelog
%autochangelog
