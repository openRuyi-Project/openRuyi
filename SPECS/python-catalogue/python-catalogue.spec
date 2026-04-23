# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname catalogue

Name:           python-%{srcname}
Version:        2.0.10
Release:        %autorelease
Summary:        Super lightweight function registries for your library
License:        MIT
URL:            https://github.com/explosion/catalogue
#!RemoteAsset:  sha256:4f56daa940913d3f09d589c191c74e5a6d51762b3a9e37dd53b7437afd6cda15
Source0:        https://files.pythonhosted.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
catalogue is a tiny, zero-dependencies library
that makes it easy to add function (or object) registries
to your code. Function registries are helpful when you have
objects that need to be both easily serializable and fully
customizable. Instead of passing a function into your object,
you pass in an identifier name, which the object can use to
lookup the function from the registry. This makes the object
easy to serialize, because the name is a simple string. If
you instead saved the function, you'd have to use Pickle
for serialization, which has many drawbacks.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
