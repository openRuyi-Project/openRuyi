# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# The packages are called python(3)-(s)rpm-macros
# We never want python3-rpm-macros to provide python-rpm-macros
# We opt out from all Python name-based automatic provides and obsoletes
%undefine __pythonname_provides
%undefine __pythonname_obsoletes

Name:           python-rpm-macros
# The package version MUST be always the same as %%{__default_python3_version}.
# To have only one source of truth, we load the macro and use it.
# The macro is defined in python-srpm-macros.
%{lua:
if posix.stat(rpm.expand('%{SOURCE1}')) then
  rpm.load(rpm.expand('%{SOURCE1}'))
elseif posix.stat('macros.python-srpm') then
  -- something is parsing the spec without _sourcedir macro properly set
  rpm.load('macros.python-srpm')
end
}
Version:        %{__default_python3_version}
Release:        %autorelease
Summary:        The common Python RPM macros
License:        MIT AND PSF-2.0 AND GPL-2.0-or-later
# Yeah I know... (sigh)
URL:            https://src.fedoraproject.org/rpms/python-rpm-macros/
# Macros
Source0:        macros.python
Source1:        macros.python-srpm
Source2:        macros.python3
Source3:        macros.pybytecompile
# Lua files
Source4:        python.lua
# Python code
%global compileall2_version 0.8.0
# From https://github.com/fedora-python/compileall2/raw/v%{compileall2_version}/compileall2.py
Source5:        compileall2.py
Source6:        import_all_modules.py
%global pathfix_version 1.0.0
# From https://github.com/fedora-python/pathfix/raw/v%{pathfix_version}/pathfix.py
Source7:        pathfix.py
Source8:        clamp_source_mtime.py
# BuildRoot Policy scripts
Source9:        brp-python-bytecompile
Source10:       brp-python-hardlink
Source11:       brp-fix-pyc-reproducibility
Source12:       brp-python-rpm-in-distinfo
BuildArch:      noarch

# For %%__default_python3_pkgversion used in %%python_provide
# For python.lua
# For compileall2.py
Requires:       python-srpm-macros = %{version}-%{release}

%description
This package contains the unversioned Python RPM macros, that most
implementations should rely on.

You should not need to install this package manually as the various
python?-devel packages require it. So install a python-devel package instead.

%package     -n python-srpm-macros
Summary:        RPM macros for building Python source packages

# For directory structure and flags macros
# Versions before 190 contained some brp scripts moved into python-srpm-macros
Requires:       rpm-config-openruyi

# Bundle something
Provides:       bundled(python3dist(compileall2)) = %{compileall2_version}

%description -n python-srpm-macros
RPM macros for building Python source packages.

%package     -n python3-rpm-macros
Summary:        RPM macros for building Python 3 packages

# For %%__python3 and %%python3
Requires:       python-srpm-macros = %{version}-%{release}

# For %%py_setup and import_all_modules.py
Requires:       python-rpm-macros = %{version}-%{release}

%description -n python3-rpm-macros
RPM macros for building Python 3 packages.

%prep
%autosetup -c -T
cp -a %{sources} .

# We want to have shebang in the script upstream but not here so
# the package with macros does not depend on Python.
sed -i '1s=^#!/usr/bin/env python3==' pathfix.py

%install
mkdir -p %{buildroot}%{_rpmmacrodir}
install -m 644 macros.* %{buildroot}%{_rpmmacrodir}/

mkdir -p %{buildroot}%{_rpmluadir}/openruyi/srpm
install -p -m 644 -t %{buildroot}%{_rpmluadir}/openruyi/srpm python.lua

mkdir -p %{buildroot}%{_rpmconfigdir}/openruyi
install -m 644 compileall2.py %{buildroot}%{_rpmconfigdir}/openruyi/
install -m 644 clamp_source_mtime.py %{buildroot}%{_rpmconfigdir}/openruyi/
install -m 644 import_all_modules.py %{buildroot}%{_rpmconfigdir}/openruyi/
install -m 644 pathfix.py %{buildroot}%{_rpmconfigdir}/openruyi/
install -m 755 brp-* %{buildroot}%{_rpmconfigdir}/openruyi/

# We define our own BRPs here to use the ones from the %%{buildroot},
# that way, this package can be built when it includes them for the first time.
# It also ensures that:
#  - our BRPs can execute
#  - if our BRPs affect this package, we don't need to build it twice
%define add_buildroot() %{lua:print((macros[macros[1]]:gsub(macros._rpmconfigdir, macros.buildroot .. macros._rpmconfigdir)))}
%global __brp_python_bytecompile %{add_buildroot __brp_python_bytecompile}
%global __brp_python_hardlink %{add_buildroot __brp_python_hardlink}
%global __brp_fix_pyc_reproducibility %{add_buildroot __brp_fix_pyc_reproducibility}
%global __brp_python_rpm_in_distinfo %{add_buildroot __brp_python_rpm_in_distinfo}

%check
# no macros in comments
grep -E '^#[^%%]*%%[^%%]' %{buildroot}%{_rpmmacrodir}/macros.* && exit 1 || true

%files
%{_rpmmacrodir}/macros.python
%{_rpmmacrodir}/macros.pybytecompile
%{_rpmconfigdir}/openruyi/import_all_modules.py
%{_rpmconfigdir}/openruyi/pathfix.py

%files -n python-srpm-macros
%{_rpmmacrodir}/macros.python-srpm
%{_rpmconfigdir}/openruyi/compileall2.py
%{_rpmconfigdir}/openruyi/clamp_source_mtime.py
%{_rpmconfigdir}/openruyi/brp-python-bytecompile
%{_rpmconfigdir}/openruyi/brp-python-hardlink
%{_rpmconfigdir}/openruyi/brp-fix-pyc-reproducibility
%{_rpmconfigdir}/openruyi/brp-python-rpm-in-distinfo
%{_rpmluadir}/openruyi/srpm/python.lua

%files -n python3-rpm-macros
%{_rpmmacrodir}/macros.python3

%changelog
%autochangelog
