# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           openruyi-minimal
Version:        1
Release:        %autorelease
Summary:        Meta package for minimal openRuyi environment
License:        MulanPSL-2.0
URL:            https://www.openruyi.org

Provides:       system-minimal

# Foundation packages
Requires:       setup
Requires:       filesystem
Requires:       system-release
Requires:       system-repos
# Base system
Requires:       coreutils
Requires:       util-linux
Requires:       bash
# Password and user management
Requires:       cracklib
Requires:       cracklib-dicts
Requires:       libpwquality
Requires:       shadow
Requires:       sudo
# Package manager
Requires:       dnf5
# Certificates
Requires:       ca-certificates
Requires:       ca-certificates-mozilla
# i18n
Requires:       glibc-gconv-modules-extra
Requires:       glibc-locale-base
# Useful tools
Requires:       curl
Requires:       nano

%description
This meta package provides the minimal environment for openRuyi.

%prep

%build

%install

%files

%changelog
%autochangelog
