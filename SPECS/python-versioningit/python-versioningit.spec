# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname versioningit

Name:           python-%{srcname}
Version:        3.3.0
Release:        %autorelease
Summary:        Versioning based on git tags for build systems
License:        MIT
URL:            https://github.com/jwodder/versioningit
#!RemoteAsset:  sha256:b91ad7d73e73d21220e69540f20213f2b729a1f9b35c04e9e137eaf28d2214da
Source0:        https://files.pythonhosted.org/packages/source/v/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
VersioningIt finds the version of a package based on VCS tags and
version config files.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/versioningit

%changelog
%autochangelog
