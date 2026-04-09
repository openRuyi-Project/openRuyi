# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           desktop-file-utils
Version:        0.28
Release:        %autorelease
Summary:        Utilities for manipulating .desktop files
License:        GPL-2.0-or-later
URL:            https://www.freedesktop.org/software/desktop-file-utils
VCS:            git:https://gitlab.freedesktop.org/xdg/desktop-file-utils.git
#!RemoteAsset
Source:         https://www.freedesktop.org/software/desktop-file-utils/releases/desktop-file-utils-%{version}.tar.xz
BuildSystem:    meson

Patch:          0001-validate-Add-Phosh-to-list-of-valid-OnlyShowIn-envir.patch

BuildRequires:  gcc
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  meson

%description
.desktop files are used to describe an application for inclusion in
GNOME or KDE menus.  This package contains desktop-file-validate which
checks whether a .desktop file complies with the specification, and
desktop-file-install which installs a desktop file to the standard directory.

%transfiletriggerin -- %{_datadir}/applications
update-desktop-database &> /null || :

%transfiletriggerpostun -- %{_datadir}/applications
update-desktop-database &> /dev/null || :

%files
%doc AUTHORS README NEWS
%license COPYING
%{_bindir}/*
%{_mandir}/man1/desktop-file-install.1*
%{_mandir}/man1/desktop-file-validate.1*
%{_mandir}/man1/update-desktop-database.1*
%{_mandir}/man1/desktop-file-edit.1*
%{_datadir}/emacs/site-lisp/desktop-entry-mode.el

%changelog
%autochangelog
