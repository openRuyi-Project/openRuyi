# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xdg-utils
Version:        1.2.1
Release:        %autorelease
Summary:        Basic desktop integration functions
License:        MIT
URL:            https://www.freedesktop.org/wiki/Software/xdg-utils/
VCS:            git:https://gitlab.freedesktop.org/xdg/xdg-utils
#!RemoteAsset
Source:         https://gitlab.freedesktop.org/xdg/xdg-utils/-/archive/v%{version}/xdg-utils-v%{version}.tar.gz
BuildSystem:    autotools

Patch0:         0001-disable-docs.patch

BuildRequires:  gawk
BuildRequires:  make

Requires:       coreutils
Requires:       desktop-file-utils
Requires:       which

%description
The xdg-utils package is a set of simple scripts that provide basic
desktop integration functions for any Free Desktop, such as Linux.
They are intended to provide a set of defacto standards.

The following scripts are provided at this time:
* xdg-desktop-icon      Install icons to the desktop
* xdg-desktop-menu      Install desktop menu items
* xdg-email             Send mail using the user's preferred e-mail composer
* xdg-icon-resource     Install icon resources
* xdg-mime              Query information about file type handling and
                        install descriptions for new file types
* xdg-open              Open a file or URL in the user's preferred application
* xdg-screensaver       Control the screensaver
* xdg-settings          Get various settings from the desktop environment

# no tests.
%check

%files
%doc ChangeLog README.md TODO
%license LICENSE
%{_bindir}/xdg-desktop-icon
%{_bindir}/xdg-desktop-menu
%{_bindir}/xdg-email
%{_bindir}/xdg-icon-resource
%{_bindir}/xdg-mime
%{_bindir}/xdg-open
%{_bindir}/xdg-screensaver
%{_bindir}/xdg-settings

%changelog
%autochangelog
