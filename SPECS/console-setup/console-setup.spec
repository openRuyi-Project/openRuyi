# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           console-setup
Version:        1.244
Release:        %autorelease
Summary:        Tools for configuring the console font and keyboard
License:        GPL-2.0-or-later AND MIT AND LicenseRef-openRuyi-Public-Domain
URL:            https://packages.debian.org/sid/console-setup
VCS:            git:https://salsa.debian.org/installer-team/console-setup.git
#!RemoteAsset
Source:         https://salsa.debian.org/installer-team/console-setup/-/archive/%{version}/console-setup-%{version}.tar.bz2
BuildSystem:    autotools

Patch0:         0001-fix-makefile.patch

BuildOption(install):  prefix=%{_prefix}
BuildOption(install):  exec_prefix=%{_exec_prefix}
BuildOption(install):  bindir=%{_bindir}
BuildOption(install):  sbindir=%{_sbindir}
BuildOption(install):  sysconfdir=%{_sysconfdir}
BuildOption(install):  datarootdir=%{_datadir}
BuildOption(install):  mandir=%{_mandir}

BuildRequires:  perl
BuildRequires:  make
BuildRequires:  bdfresize
BuildRequires:  otf2bdf
BuildRequires:  unifont
BuildRequires:  fonts-dejavu
Requires:       kbd

%description
This package provides tools to configure the console's font and keyboard layout,
often using settings derived from the X Window System.

%package     -n bdf2psf
Summary:    Generate console fonts from BDF source fonts

%description -n bdf2psf
This package provides a command-line converter to build console fonts from BDF
sources.

%prep -a
# Adapt DejaVu path to where oR installs it
sed -i "s@/usr/share/fonts/truetype/dejavu@"%{_datadir}"/fonts/truetype@g" Fonts/Makefile

# No configure
%conf

%build -p
# Build all BDF fonts
make bdf

# No tests
%check

%files
%doc README debian/changelog
%license COPYRIGHT copyright.fonts copyright.xkb Fonts/copyright
%{_bindir}/ckbcomp
%{_bindir}/setupcon
%config(noreplace) %{_sysconfdir}/default/console-setup
%config(noreplace) %{_sysconfdir}/default/keyboard
%{_datadir}/consolefonts/
%{_datadir}/consoletrans/
%{_mandir}/man1/ckbcomp.1*
%{_mandir}/man1/setupcon.1*
%{_mandir}/man5/console-setup.5*
%{_mandir}/man5/keyboard.5*

%files -n bdf2psf
%license GPL-2
%{_bindir}/bdf2psf
%{_mandir}/man1/bdf2psf.1*
%{_datadir}/bdf2psf/

%changelog
%autochangelog
