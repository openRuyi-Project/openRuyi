# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global flavor @BUILD_FLAVOR@%{nil}
%global srcname setuptools
%global python_wheel_name %{srcname}-%{version}-py3-none-any.whl

# Virtual provides for the packages bundled by setuptools.
# Bundled packages are defined in multiple files. Generate the list with:
# pip freeze --path setuptools/_vendor > vendored.txt
# %%{_rpmconfigdir}/pythonbundles.py --namespace 'python%3dist' vendored.txt
%global bundled %{expand:
Provides: bundled(python3dist(autocommand)) = 2.2.2
Provides: bundled(python3dist(backports-tarfile)) = 1.2
Provides: bundled(python3dist(importlib-metadata)) = 8
Provides: bundled(python3dist(inflect)) = 7.3.1
Provides: bundled(python3dist(jaraco-collections)) = 5.1
Provides: bundled(python3dist(jaraco-context)) = 5.3
Provides: bundled(python3dist(jaraco-functools)) = 4.0.1
Provides: bundled(python3dist(jaraco-text)) = 3.12.1
Provides: bundled(python3dist(more-itertools)) = 10.3
Provides: bundled(python3dist(packaging)) = 24.2
Provides: bundled(python3dist(platformdirs)) = 4.2.2
Provides: bundled(python3dist(tomli)) = 2.0.1
Provides: bundled(python3dist(typeguard)) = 4.3
Provides: bundled(python3dist(typing-extensions)) = 4.12.2
Provides: bundled(python3dist(wheel)) = 0.45.1
Provides: bundled(python3dist(zipp)) = 3.19.2
}

# If it is set to 1, the bootstrap process will be included
%if "%{flavor}" == "bootstrap"
%bcond bootstrap 1
%else
%bcond bootstrap 0
%endif

%if %{with bootstrap}
Name:           python-%{srcname}-bootstrap
%else
Name:           python-%{srcname}
%endif
Version:        80.9.0
Release:        %autorelease
Summary:        Easily build and distribute Python packages
License:        MIT AND Apache-2.0 AND (BSD-2-Clause OR Apache-2.0) AND Python-2.0.1 AND LGPL-3.0-only
URL:            https://pypi.python.org/pypi/setuptools
# TODO: Use %%{pypi_source %%{srcname} %%{version}} in the future - 251
#       Otherwise https://files.pythonhosted.org/packages/source/a/abc/%%{srcname}-%%{version}.tar.gz
#!RemoteAsset:  sha256:f36b47402ecde768dbfafc46e8e4207b4360c654f1f3bb84475f0a28628fb19c
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

# setuptools rewrites all shebangs to "#!python" which breaks workflows
# where no external installers (usually rewriting this) are involved.
# https://github.com/pypa/setuptools/issues/4883
# - Resolution: deprecated functionality won't be fixed.
# brp-mangle-shebang script cannot mangle this and fails for many pkgs.
Patch0:         0001-Revert-Always-rewrite-a-Python-shebang-to-python.patch

BuildRequires:  pkgconfig(python3)

%if %{with bootstrap}
BuildRequires:  unzip
%endif

# python3 bootstrap: this is built before the final build of python3, which
# adds the dependency on python3-rpm-generators, so we require it manually
BuildRequires:  python3-rpm-generators
# we also use %%{_pyproject_wheeldir}, so an explicit requirement on the pyproject-macros is needed
BuildRequires:  pyproject-rpm-macros

%if %{without bootstrap}
# Not to use the pre-generated egg-info, we use setuptools from previous build to generate it
BuildRequires:  python3-setuptools
%endif

%{bundled}

# For users who might see ModuleNotFoundError: No module named 'pkg_resoureces'
# NB: Those are two different provides: one contains underscore, the other hyphen
%py_provides    python3-pkg_resources
%py_provides    python3-pkg-resources

%description
Setuptools is a collection of enhancements to the Python distutils that allow
you to more easily build and distribute Python packages, especially ones that
have dependencies on other packages.

This package also contains the runtime components of setuptools, necessary to
execute the software that requires pkg_resources.

%package     -n %{python_wheel_pkg_prefix}-%{srcname}-wheel
Summary:        The setuptools wheel
%{bundled}

%description -n %{python_wheel_pkg_prefix}-%{srcname}-wheel
A Python wheel of setuptools to use with venv.

%prep
%autosetup -p1 -n %{srcname}-%{version}

# Strip shbang
find setuptools pkg_resources -name \*.py | xargs sed -i -e '1 {/^#!\//d}'
# Remove bundled exes
rm -f setuptools/*.exe
# Don't ship these
rm -r docs/conf.py

%if %{without bootstrap}
%generate_buildrequires
%pyproject_buildrequires -r
%endif

%build
%if %{with bootstrap}
%{python3} setup.py bdist_wheel
mkdir -p %{_pyproject_wheeldir}
mv dist/%{python_wheel_name} %{_pyproject_wheeldir}
%else
%pyproject_wheel
%endif

%install
%if %{with bootstrap}
mkdir -p %{buildroot}%{python3_sitelib}
unzip %{_pyproject_wheeldir}/%{python_wheel_name} -d %{buildroot}%{python3_sitelib} -x setuptools-%{version}.dist-info/RECORD
echo rpm > %{buildroot}%{python3_sitelib}/setuptools-%{version}.dist-info/INSTALLER
%else
%pyproject_install
%pyproject_save_files -l setuptools pkg_resources _distutils_hack
sed -Ei '/\/tests\b/d' %{pyproject_files}
%endif

# https://github.com/pypa/setuptools/issues/2709
find %{buildroot}%{python3_sitelib} -name tests -print0 | xargs -0 rm -r

# Install the wheel for the python-setuptools-wheel package
mkdir -p %{buildroot}%{python_wheel_dir}
install -p %{_pyproject_wheeldir}/%{python_wheel_name} -t %{buildroot}%{python_wheel_dir}

%files %{?!with_bootstrap:-f %{pyproject_files}}
%doc docs/* NEWS.rst README.rst
%{python3_sitelib}/distutils-precedence.pth
%if %{with bootstrap}
%{python3_sitelib}/setuptools-%{version}.dist-info/
%license %{python3_sitelib}/setuptools-%{version}.dist-info/licenses/LICENSE
%{python3_sitelib}/pkg_resources/
%{python3_sitelib}/setuptools/
%{python3_sitelib}/_distutils_hack/
%endif

%files -n %{python_wheel_pkg_prefix}-%{srcname}-wheel
%license LICENSE
# we own the dir for simplicity
%dir %{python_wheel_dir}/
%{python_wheel_dir}/%{python_wheel_name}

%changelog
%autochangelog
