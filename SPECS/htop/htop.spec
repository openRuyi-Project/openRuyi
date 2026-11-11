# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           htop
Version:        3.5.3
Release:        %autorelease
Summary:        An interactive process viewer
License:        GPL-2.0-or-later
URL:            https://htop.dev
VCS:            git:https://github.com/htop-dev/htop
#!RemoteAsset:  sha256:edf25ee020a5263ffbef9eef5a8c14392bf74e78b3d5c8bc64d9343dd9a82605
Source0:        https://github.com/htop-dev/htop/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  pkgconfig(ncurses)
BuildRequires:  autoconf
BuildRequires:  automake
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
