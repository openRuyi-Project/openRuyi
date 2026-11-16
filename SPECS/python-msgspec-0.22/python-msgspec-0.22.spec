# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: A.Donz <avrova.minix@donz.si>
# SPDX-FileContributor: MMLA-org <https://github.com/MMLA-org>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global pypi_name msgspec

# This recipe intentionally shadows the python-msgspec recipe owned by a
# different contributor, which stays at 0.19.0.  msgspec 0.20.0 is the first
# release that understands Python 3.14 lazy annotations (PEP 649): 0.19.0
# advertises no struct fields at all under 3.14 because its C extension reads
# __annotations__ from the instance __dict__ instead of the module's
# __annotate_func__.  Consumers that build msgspec.Struct subclasses at import
# time therefore need 0.22.0 here.
#
# The two recipes install the same site-packages/msgspec/ directory, so rpm
# cannot keep both installed: the file lists would collide on every shared
# path.  Obsoletes below makes this package replace python-msgspec during the
# transaction, which removes the 0.19.0 payload before the new files land.
Name:           python-%{pypi_name}-0.22
Version:        0.22.0
Release:        %autorelease
Summary:        Fast serialization and validation library
License:        BSD-3-Clause
URL:            https://jcristharif.com/msgspec/
#!RemoteAsset:  sha256:0a13624a4969159fe35d8c2a3d377b2b61bbd8585e327440d5e52725affcce38
Source0:        https://files.pythonhosted.org/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildSystem:    pyproject

# The archive directory is msgspec-0.22.0, while the expanded Name also
# carries the version suffix for the package name.
BuildOption(prep):  -n %{pypi_name}-%{version}
BuildOption(install):  %{pypi_name}
# Importing the module proves the compiled _core extension loads.
BuildOption(check):  %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-devel
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools) >= 80
# Upstream pyproject.toml declares setuptools>=80 and setuptools-scm>=8 as its
# build backend.  The sdist ships no Git metadata, so the version is supplied
# through SETUPTOOLS_SCM_PRETEND_VERSION below rather than derived from a tag.
BuildRequires:  python3dist(setuptools-scm) >= 8
BuildRequires:  python3dist(wheel)

Obsoletes:      python-msgspec < 0.22.0
Provides:       python-msgspec = %{version}-%{release}
Provides:       python3-%{pypi_name} = %{version}-%{release}
Provides:       python3-%{pypi_name}%{?_isa} = %{version}-%{release}
%python_provide python3-%{pypi_name}

%description
A fast serialization and validation library, with builtin support for
JSON, MessagePack, YAML, and TOML.

%generate_buildrequires
# msgspec has no required runtime dependencies.  The upstream optional extras
# (tomli_w, PyYAML) are not dependencies of this package and must not be
# pulled in by the build backend resolution, hence -R.
%pyproject_buildrequires -R

%build -p
# Without Git metadata setuptools-scm cannot derive a version from the archive.
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'

%install -a

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
