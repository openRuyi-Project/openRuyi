# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# amdSMI's gtest client (amdsmitst) needs GPU/driver to run
%bcond run_test 0

%global rocm_release 7.2
%global rocm_patch 4
%global rocm_version %{rocm_release}.%{rocm_patch}

%global esmi_ver 4.2
%global pkg_library_version 26

Name:           amdsmi
Version:        %{rocm_version}
Release:        %autorelease
Summary:        AMD System Management Interface
# Main license is MIT
#
# include/amd_smi/impl/amd_hsmp.h
# esmi_ib_library/include/asm/amd_hsmp.h
# Both carry: SPDX-License-Identifier: GPL-2.0 WITH Linux-syscall-note
#
# Bundled esmi_ib_library is NCSA
License:        MIT AND (GPL-2.0-only WITH Linux-syscall-note) AND NCSA
URL:            https://github.com/ROCm/amdsmi
#!RemoteAsset:  sha256:1075067f450860313445edc97026ba430c33e93c18a9c1b1440d71a1f210d1cb
Source0:        %{url}/archive/rocm-%{version}.tar.gz
#!RemoteAsset:  sha256:de19d222d09e2171f47f8bbd6608e5648bd547c82543379bb8fb5ed2e379e141
Source1:        https://github.com/amd/esmi_ib_library/archive/refs/tags/esmi_pkg_ver-%{esmi_ver}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -G Ninja
BuildOption(conf):  -DBUILD_TESTS=ON
BuildOption(conf):  -DCMAKE_SKIP_INSTALL_RPATH=TRUE
%ifnarch x86_64
BuildOption(conf):  -DENABLE_ESMI_LIB=OFF
%endif

BuildRequires:  cmake
BuildRequires:  cmake(GTest)
BuildRequires:  ninja
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libdrm_amdgpu)
BuildRequires:  pkgconfig(python3)

Requires:       python3dist(pyyaml)

%patchlist
# Support libdrm 2.4.130+
# https://github.com/ROCm/amdsmi/pull/165
0001-Fix-compilation-with-libdrm-2.4.130.patch
# -DENABLE_ESMI_LIB=OFF is not enough
# Goamdshim calls CPU/ESMI-only APIs; skip building it when ESMI is off
2001-Disable-goamdsmi_shim-when-ESMI-is-off.patch
# libamd_smi.so may lack ESMI symbols; the generated ctypesgen wrapper
# binds them eagerly at import — patch it to lazy-load them instead
2002-Tolerate-missing-CPU-E-SMI-symbols.patch

%global _description %{expand:
The AMD System Management Interface Library, or AMD SMI library, is a C
library for Linux that provides a user space interface for applications
to monitor and control AMD devices.
}

%description
%{_description}

%package        devel
Summary:        Libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
%{_description}

%package        test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    test
%{_description}

%prep
%autosetup -p1 -C

# ESMI - EPYC System Management Interface
# esmi_ib_library uses x86-only cpuid.h; guard it for non-x86 builds
%ifarch x86_64
tar xf %{SOURCE1}
mv esmi_ib_library-* esmi_ib_library
mv esmi_ib_library/License.txt esmi_ib_library_License.txt
# The esmi version check uses git tags, but we use tar's without git files.
# Just inject in the tag that we've pulled into the version check:
sed -i 's/NOT latest_esmi_tag/NOT "esmi_pkg_ver-%{esmi_ver}"/' CMakeLists.txt
%endif

# Fix script shebang
sed -i -e 's@env python3@python3@' amdsmi_cli/*.py

%install -a
mkdir -p %{buildroot}%{python3_sitearch}
mv %{buildroot}%{_datadir}/amdsmi %{buildroot}%{python3_sitearch}
mv %{buildroot}%{_datadir}/pyproject.toml %{buildroot}%{python3_sitearch}/amdsmi/

# W: unstripped-binary-or-object .../amdsmi/libamd_smi.so
# Does an explicit open, so can not just rm it; strip it instead
strip %{buildroot}%{python3_sitearch}/amdsmi/*.so
# E: non-executable-script .../amdsmi_cli/amdsmi_cli_exceptions.py 644 /usr/bin/env python3
chmod a+x %{buildroot}%{_libexecdir}/amdsmi_cli/amdsmi_*.py

rm -f %{buildroot}%{_datadir}/_version.py
rm -f %{buildroot}%{_datadir}/amd_smi/_version.py
rm -rvf %{buildroot}%{_datadir}/amd_smi/example
rm -f %{buildroot}%{_datadir}/amd_smi/setup.py
rm -rvf %{buildroot}%{_datadir}/example
rm -f %{buildroot}%{_datadir}/setup.py
rm -f %{buildroot}%{_docdir}/amd-smi-lib/LICENSE.txt
rm -f %{buildroot}%{_docdir}/amd-smi-lib/README.md
rm -rvf %{buildroot}%{_docdir}/amd-smi-lib/copyright
rm -f %{buildroot}%{_docdir}/amd_smi-asan/LICENSE.txt

if [ -e %{buildroot}%{_datadir}/tests ]; then
    mkdir -p %{buildroot}%{_datadir}/amdsmi
    mv %{buildroot}%{_datadir}/tests %{buildroot}%{_datadir}/amdsmi/tests
fi

# amdsmitst needs GPU/driver access to run
%if %{without run_test}
%check
%endif

%files
%doc README.md
%license LICENSE
%{_bindir}/amd-smi
%{_libdir}/libamd_smi.so.%{pkg_library_version}{,.*}
%{_libexecdir}/amdsmi_cli
%{python3_sitearch}/amdsmi
%ifarch x86_64
%license esmi_ib_library_License.txt
%{_libdir}/libgoamdsmi_shim64.so.1{,.*}
%endif

%files devel
%{_includedir}/amd_smi/
%{_libdir}/cmake/amd_smi/
%{_libdir}/libamd_smi.so
%ifarch x86_64
%{_includedir}/*.h
%{_libdir}/libgoamdsmi_shim64.so
%endif

%files test
%{_datadir}/amdsmi/

%changelog
%autochangelog
