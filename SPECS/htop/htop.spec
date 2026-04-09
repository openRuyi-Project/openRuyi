# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           htop
Version:        3.4.1
Release:        %autorelease
Summary:        An interactive process viewer
License:        GPL-2.0-or-later
URL:            https://htop.dev
VCS:            git:https://github.com/htop-dev/htop
#!RemoteAsset
Source0:        https://github.com/htop-dev/htop/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  pkgconfig(ncurses)
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc

%description
htop is a cross-platform interactive process viewer. It allows scrolling the
list of processes, and provides an overview of system resource consumption.
Tasks related to processes (e.g. killing and renicing) can be done without
entering their PIDs.

%conf -p
./autogen.sh

%files
%license COPYING
%{_bindir}/htop
%{_datadir}/applications/htop.desktop
%{_datadir}/icons/hicolor/scalable/apps/htop.svg
%{_datadir}/pixmaps/htop.png
%{_mandir}/man1/htop.1*

%changelog
%autochangelog
