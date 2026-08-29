# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname matplotlib

Name:           python-%{srcname}
Version:        3.11.0
Release:        %autorelease
Summary:        Python library for creating static, animated, and interactive visualizations
License:        PSF-2.0 AND MIT AND CC0-1.0 AND OFL-1.1 AND Bitstream-Vera AND LicenseRef-openRuyi-Public-Domain
URL:            https://matplotlib.org
VCS:            git:https://github.com/matplotlib/matplotlib.git
#!RemoteAsset:  sha256:68c0c7be01b30dcca3638934f7f591df73401235cbdbf0d1ab1c71e7db7f8b57
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

# Use distribution libraries instead of the copies bundled in the sdist.
BuildOption(build):  -Csetup-args=-Dsystem-freetype=true
BuildOption(build):  -Csetup-args=-Dsystem-libraqm=true
BuildOption(build):  -Csetup-args=-Dsystem-qhull=true
BuildOption(install):  %{srcname} mpl_toolkits pylab -L
BuildOption(check):  -t

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(qhull_r)
BuildRequires:  pkgconfig(raqm)
BuildRequires:  python3dist(contourpy) >= 1.0.1
BuildRequires:  python3dist(cycler) >= 0.10
BuildRequires:  python3dist(fonttools) >= 4.22.0
BuildRequires:  python3dist(kiwisolver) >= 1.3.1
BuildRequires:  python3dist(meson-python) >= 0.13.2
BuildRequires:  python3dist(numpy) >= 1.25
BuildRequires:  python3dist(packaging) >= 20.0
BuildRequires:  python3dist(pillow) >= 9
BuildRequires:  python3dist(pybind11) >= 2.13.2
BuildRequires:  python3dist(pyparsing) >= 3
BuildRequires:  python3dist(python-dateutil) >= 2.7
BuildRequires:  python3dist(setuptools-scm) >= 7

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Matplotlib is a comprehensive library for creating static, animated, and
interactive visualizations in Python. It produces publication-quality figures
in a variety of hardcopy formats and interactive environments across
platforms.

%prep -a
# The upper bound only works around editable-install versioning; wheel builds
# are compatible with setuptools-scm 10, which is packaged by openRuyi.
sed -i 's/setuptools_scm>=7,<10/setuptools_scm>=7/g' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -p

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
