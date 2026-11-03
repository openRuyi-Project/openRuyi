# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname fontparts

Name:           python-%{srcname}
Version:        1.1.1
Release:        %autorelease
Summary:        Python interface for editing font objects
License:        MIT
URL:            https://github.com/robotools/fontParts
#!RemoteAsset:  sha256:7ceed66dc176c05f2274e9d09b401b124ce00c46e758e4fecb7f5f19f3d34c61
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l fontParts

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
FontParts provides a common Python interface for reading and editing
font contours, glyphs and font metadata.

# The sdist already records its release version. Match the tag_regex setting
# understood by the distribution's vcs-versioning backend.
%prep -a
sed -i -e '/^\[tool.setuptools_scm.tag\]/,/^$/d' \
    -e '/^\[tool.setuptools_scm\]/a tag_regex = "^v?(?P<version>[0-9]+(?:[.][0-9]+)*)$"' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
