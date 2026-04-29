# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           python-systemd
Version:        235
Release:        %autorelease
Summary:        Python module wrapping libsystemd functionality
License:        LGPL-2.1-or-later
URL:            https://github.com/systemd/python-systemd
#!RemoteAsset:  sha256:38181dbd451fd418d316a92a34bc2118967930684cdd62c3e979fe8c8ebacffa
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    pyproject

# https://github.com/systemd/python-systemd/pull/140
Patch0:         0001-docs-update-intersphinx-_-mapping.patch

BuildOption(install):  systemd +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  pkgconfig(libsystemd)

Provides:       python3-systemd = %{version}-%{release}
Provides:       python3-systemd%{?_isa} = %{version}-%{release}
%python_provide python3-systemd

%description
Python module for native access to the libsystemd facilities. Functionality
includes sending of structured messages to the journal and reading journal
files, querying machine and boot identifiers and a lists of message identifiers
provided by systemd. Other functionality provided the library is also wrapped.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README*
%license LICENSE.txt

%changelog
%autochangelog
