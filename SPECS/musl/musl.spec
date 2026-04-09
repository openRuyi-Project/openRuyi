# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: ayostl <yao_xp@yeah.net>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _musl_target_cpu %{_target_cpu}
%global _musl_platform %{_musl_target_cpu}-linux-musl

%global _libdir %{_prefix}/lib/%{_musl_platform}
%global _includedir %{_prefix}/include/%{_musl_platform}

%global _syslibdir /lib

Name:           musl
Version:        1.2.5
Release:        %autorelease
Summary:        Fully featured lightweight standard C library for Linux
License:        MIT
URL:            https://musl.libc.org
#!RemoteAsset
Source0:        %{url}/releases/%{name}-%{version}.tar.gz
#!RemoteAsset
Source1:        %{url}/releases/%{name}-%{version}.tar.gz.asc
BuildSystem:    autotools

# Support PIE with static linking
Patch0:         0001-musl-1.2.0-Support-static-pie-with-musl-gcc-specs.patch

BuildOption(conf):  --enable-debug
BuildOption(conf):  --enable-wrapper=all

BuildRequires:  gcc
BuildRequires:  make

%description
musl is a C standard library to power a new generation
of Linux-based devices. It is lightweight, fast, simple,
free, and strives to be correct in the sense of standards
conformance and safety.

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-headers = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
musl is a C standard library to power a new generation
of Linux-based devices. It is lightweight, fast, simple,
free, and strives to be correct in the sense of standards
conformance and safety.

This package provides the development files for using
musl with programs and libraries.

%package        static
Summary:        Static link library for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    static
musl is a C standard library to power a new generation
of Linux-based devices. It is lightweight, fast, simple,
free, and strives to be correct in the sense of standards
conformance and safety.

This package provides the additional development files for
statically linking musl into programs and libraries.

%package        gcc
Summary:        Wrapper for using gcc with musl
Requires:       %{name}-devel = %{version}-%{release}
Requires:       gcc

%description    gcc
musl is a C standard library to power a new generation
of Linux-based devices. It is lightweight, fast, simple,
free, and strives to be correct in the sense of standards
conformance and safety.

This package provides a wrapper around gcc to compile
programs and libraries with musl easily.

%package        clang
Summary:        Wrapper for using clang with musl
Requires:       %{name}-devel = %{version}-%{release}
Requires:       clang

%description    clang
musl is a C standard library to power a new generation
of Linux-based devices. It is lightweight, fast, simple,
free, and strives to be correct in the sense of standards
conformance and safety.

This package provides a wrapper around clang to compile
programs and libraries with musl easily.

%build -p
# musl is known not to work with LTO
# Disable LTO
%define _lto_cflags %{nil}

# Set linker flags to get correct soname...
export LDFLAGS="%{?build_ldflags} -Wl,-soname,ld-musl-%{_musl_target_cpu}.so.1"

%install -a
# Swap the files around for libc.so, making libc.so a symlink to the real file
rm %{buildroot}/lib/ld-musl-%{_musl_target_cpu}.so.1
mv %{buildroot}%{_libdir}/libc.so %{buildroot}/lib/ld-musl-%{_musl_target_cpu}.so.1
ln -sr %{buildroot}/lib/ld-musl-%{_musl_target_cpu}.so.1 %{buildroot}%{_libdir}/ld-musl-%{_musl_target_cpu}.so.1
ln -sr %{buildroot}%{_libdir}/ld-musl-%{_musl_target_cpu}.so.1 %{buildroot}%{_libdir}/libc.so

# Write search path for dynamic linker
mkdir -p %{buildroot}%{_sysconfdir}
touch %{buildroot}%{_sysconfdir}/ld-musl-%{_musl_target_cpu}.path
cat > %{buildroot}%{_sysconfdir}/ld-musl-%{_musl_target_cpu}.path <<EOF
%{_libdir}
EOF

mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d
touch %{buildroot}%{_rpmconfigdir}/macros.d/macros.musl
cat > %{buildroot}%{_rpmconfigdir}/macros.d/macros.musl <<EOF
%%_musl_libdir %{_libdir}
%%_musl_includedir %{_includedir}
EOF

# musl no test
%check

%files
%license COPYRIGHT
/lib/ld-musl-%{_musl_target_cpu}.so.1
%{_libdir}/ld-musl-%{_musl_target_cpu}.so.1
%config(noreplace) %{_sysconfdir}/ld-musl-%{_musl_target_cpu}.path

%files devel
%license COPYRIGHT
%doc README WHATSNEW
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.o
%{_libdir}/*.a
%exclude %{_libdir}/libc.a
%{_rpmconfigdir}/macros.d/macros.musl

%files static
%license COPYRIGHT
%{_libdir}/libc.a

%files gcc
%license COPYRIGHT
%{_bindir}/musl-gcc
%{_libdir}/musl-gcc.specs

%files clang
%license COPYRIGHT
%{_bindir}/musl-clang
%{_bindir}/ld.musl-clang

%changelog
%autochangelog
