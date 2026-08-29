# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname docopt-ng
%global pypi_name docopt_ng

Name:           python-%{srcname}
Version:        0.9.0
Release:        %autorelease
Summary:        Jazzband-maintained fork of docopt, the humane command line arguments parser.
License:        MIT
URL:            https://github.com/jazzband/docopt-ng
#!RemoteAsset:  sha256:91c6da10b5bb6f2e9e25345829fb8278c78af019f6fc40887ad49b060483b1d7
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  docopt +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This library allows the user to define a command-line
interface from a program's help message rather than specifying it
programmatically with command-line parsers like getopt and
argparse.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README*
%license LICENSE-MIT

%changelog
%autochangelog
