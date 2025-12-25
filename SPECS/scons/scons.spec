# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           scons
Version:        4.9.1
Release:        %autorelease
Summary:        A modern build tool, a replacement for Make
License:        MIT
URL:            https://www.scons.org/
#!RemoteAsset
Source:         https://sourceforge.net/projects/scons/files/scons/%{version}/SCons-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install): -l SCons  +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
%py_provides    scons-python3
%py_provides    python3-%{name}
%py_provides    SCons
%py_provides    scons

%description

SCons is a software construction tool. It is an improved, cross-platform
substitute for the classic Make utility with integrated functionality similar
to Autoconf/Automake and compiler caches such as ccache.


%generate_buildrequires
%pyproject_buildrequires

# No check
%check

%files -f %{pyproject_files}

%changelog
%{?autochangelog}
