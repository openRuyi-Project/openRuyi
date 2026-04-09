# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           qalculate-qt
Version:        5.9.0.1
Release:        %autorelease
Summary:        Powerful and easy to use calculator
License:        GPL-2.0-or-later AND CC0-1.0
URL:            https://qalculate.github.io/
VCS:            git:https://github.com/Qalculate/qalculate-qt
#!RemoteAsset:  sha256:e4efb8c4df594e65781bd60add020ab154c62e07422530907792aecaad4cf646
Source0:        https://github.com/Qalculate/qalculate-qt/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    autotools

BuildOption(install):  INSTALL_ROOT='%{buildroot}'

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  qt6-linguist
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(libqalculate)
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(mpfr)

%description
Qalculate! is a multi-purpose cross-platform desktop calculator. It is simple
to use but provides power and versatility normally reserved for complicated
math packages.

%conf
# No configure.

%build
%{qmake6} PREFIX=%{_prefix}

%install -a
%find_lang %{name} --generate-subpackages --with-qt

%files -f %{name}.lang
%license COPYING
%doc AUTHORS README
%{_bindir}/qalculate-qt
%{_mandir}/man1/qalculate-qt.1*
%{_datadir}/icons/hicolor/*/*/qalculate*
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/*.metainfo.xml
%dir %{_datadir}/qalculate-qt
%dir %{_datadir}/qalculate-qt/translations

%changelog
%autochangelog
