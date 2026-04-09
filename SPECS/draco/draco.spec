# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: ayostl <yao_xp@yeah.net>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Disable test until a proper fix occurs
%global         gtestflag 0

Name:           draco
Version:        1.5.7
Release:        %autorelease
Summary:        A library for compressing and decompressing 3D geometric meshes and point clouds
License:        Apache-2.0
URL:            https://github.com/google/draco
#!RemoteAsset
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildSystem:    cmake

# Downstream-only patch that unconditionally links a system copy of gtest,
# rather than expecting a git submodule as upstream prefers (and gtest upstream
# would recommend).
Patch0:         0001-Use-system-gtest.patch

BuildOption(conf):  -GNinja
BuildOption(conf):  -DBUILD_SHARED_LIBS=ON
BuildOption(conf):  -DCMAKE_BUILD_TYPE=Release
BuildOption(conf):  -DDRACO_TESTS=%{gtestflag}

BuildRequires:  cmake
%if %{?gtestflag}
BuildRequires:  cmake(gtest)
%endif
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  ninja
BuildRequires:  pkgconfig(python3)

%description
A library for compressing and decompressing 3D geometric meshes and point clouds

%package        devel
Summary:        Development files for draco
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
%{summary}.

%package        static
Summary:        Static files for draco
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    static
%{summary}.

%prep -a

# Remove precompiled CSS and Javascript along binaries
rm -fr {javascript,maya,docs/assets}

%install -a
# Create missing man files downstream
mkdir -p %{buildroot}%{_mandir}/man1
LD_LIBRARY_PATH=%{buildroot}%{_libdir} help2man -N --version-string=%{version} \
        -o %{buildroot}%{_mandir}/man1/%{name}_decoder-%{version}.1 \
        %{buildroot}%{_bindir}/%{name}_decoder
LD_LIBRARY_PATH=%{buildroot}%{_libdir} help2man -N --version-string=%{version} \
        -o %{buildroot}%{_mandir}/man1/%{name}_encoder-%{version}.1 \
        %{buildroot}%{_bindir}/%{name}_encoder

%if %{?gtestflag}
%check
%endif

%files
%license LICENSE AUTHORS
%doc README.md
%{_bindir}/draco_decoder
%{_bindir}/draco_decoder-%{version}
%{_bindir}/draco_encoder
%{_bindir}/draco_encoder-%{version}
%{_libdir}/libdraco.so.9
%{_libdir}/libdraco.so.9.0.0
%{_mandir}/man1/draco_decoder-%{version}.1*
%{_mandir}/man1/draco_encoder-%{version}.1*

%files devel
%{_includedir}/draco/
%{_datadir}/cmake/draco/
%{_libdir}/libdraco.so
%{_libdir}/pkgconfig/draco.pc

%files static
%{_libdir}/libdraco.a

%changelog
%autochangelog
