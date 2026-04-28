# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname thinc

Name:           python-%{srcname}
Version:        8.3.10
Release:        %autorelease
Summary:        A refreshing functional take on deep learning, compatible with your favorite libraries
License:        MIT
URL:            https://github.com/explosion/thinc
#!RemoteAsset:  sha256:5a75109f4ee1c968fc055ce651a17cb44b23b000d9e95f04a4d047ab3cb3e34e
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
# Test cases do not need to check imports
BuildOption(check):  -e "thinc.tests.*"

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(cymem)
BuildRequires:  python3dist(preshed)
BuildRequires:  python3dist(murmurhash)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(mypy)
BuildRequires:  python3dist(blis)
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(catalogue)
BuildRequires:  python3dist(confection)
BuildRequires:  python3dist(pydantic)
BuildRequires:  python3dist(srsly)
BuildRequires:  python3dist(wasabi)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Thinc is a lightweight deep learning library that offers an elegant,
type-checked, functional-programming API for composing models, with
support for layers defined in other frameworks such as PyTorch,
TensorFlow and MXNet. You can use Thinc as an interface layer,
a standalone toolkit or a flexible way to develop new models.
Previous versions of Thinc have been running quietly in production
in thousands of companies, via both spaCy and Prodigy. We wrote the
new version to let users compose, configure and deploy custom
models built with their favorite framework.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
