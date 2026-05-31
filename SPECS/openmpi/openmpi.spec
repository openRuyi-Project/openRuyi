# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           openmpi
Version:        5.0.10
Release:        %autorelease
Summary:        Open Message Passing Interface implementation
License:        BSD-3-Clause-Open-MPI AND mpich2 AND BSD-3-Clause AND BSD-4-Clause-UC
URL:            https://www.open-mpi.org/
VCS:            git:https://github.com/open-mpi/ompi.git
#!RemoteAsset:  sha256:0acecc4fc218e5debdbcb8a41d182c6b0f1d29393015ed763b2a91d5d7374cc6
Source0:        https://download.open-mpi.org/release/open-mpi/v5.0/openmpi-%{version}.tar.bz2
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-oshmem
BuildOption(conf):  --with-libevent=external
BuildOption(conf):  --with-hwloc=external
BuildOption(conf):  --with-pmix=external
BuildOption(conf):  --with-prrte=external
BuildOption(conf):  --without-ucx
BuildOption(conf):  --without-ofi
BuildOption(conf):  --without-slurm
BuildOption(conf):  --without-pbs
BuildOption(conf):  --without-lsf
BuildOption(conf):  --without-sge
BuildOption(conf):  --without-tm
# GCC 16 rejects Open MPI's always_inline part/persist code.
BuildOption(conf):  opal_cv_cc_finline_functions=0
BuildOption(conf):  opal_cv___attribute__always_inline=0

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(hwloc) >= 1.11.0
BuildRequires:  pkgconfig(libevent) >= 2.0.21
BuildRequires:  pkgconfig(pmix) >= 5.0.0
BuildRequires:  prrte-devel
BuildRequires:  pkgconfig(zlib)

Requires:       prrte%{?_isa}

%description
Open MPI is an open source implementation of the Message Passing
Interface specification. It provides MPI runtime libraries, command
line launchers, and compiler wrappers for building MPI applications.

%package        devel
Summary:        Development files for Open MPI
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gcc
Requires:       gcc-c++
Requires:       gcc-fortran
Requires:       pkgconfig(hwloc) >= 1.11.0
Requires:       pkgconfig(libevent) >= 2.0.21
Requires:       pkgconfig(pmix) >= 5.0.0
Requires:       prrte-devel

%description    devel
This package contains Open MPI headers, pkg-config metadata, shared
object symbolic links, and compiler wrapper tools used to build MPI
applications.

%package        doc
Summary:        Documentation for Open MPI
BuildArch:      noarch

%description    doc
HTML documentation for Open MPI.

%install -a
# not installs an oshrun alias through mpirun
rm -f %{buildroot}%{_bindir}/oshrun
find %{buildroot}%{_libdir} -name '*.la' -delete

%files
%doc AUTHORS README.md VERSION
%license LICENSE
%config(noreplace) %{_sysconfdir}/openmpi-mca-params.conf
%config(noreplace) %{_sysconfdir}/openmpi-totalview.tcl
%{_bindir}/mpiexec
%{_bindir}/mpirun
%{_bindir}/ompi_info
%{_libdir}/libmpi*.so.*
%{_libdir}/libopen-pal*.so.*
%dir %{_libdir}/openmpi
%{_libdir}/openmpi/*.so
%dir %{_datadir}/openmpi
%exclude %{_datadir}/openmpi/*-wrapper-data.txt
%{_datadir}/openmpi/*
%{_mandir}/man1/mpisync.1*
%{_mandir}/man1/mpirun.1*
%{_mandir}/man1/ompi_info.1*
%{_mandir}/man7/Open-MPI.7*

%files devel
%{_bindir}/mpiCC
%{_bindir}/mpic++
%{_bindir}/mpicc
%{_bindir}/mpicxx
%{_bindir}/mpif77
%{_bindir}/mpif90
%{_bindir}/mpifort
%{_bindir}/opal_wrapper
%{_includedir}/*.h
%{_includedir}/openmpi/
%{_libdir}/libmpi*.so
%{_libdir}/libopen-pal*.so
%{_libdir}/mpi*.mod
%{_libdir}/pmpi*.mod
%{_libdir}/pkgconfig/ompi*.pc
%{_datadir}/openmpi/*-wrapper-data.txt
%{_mandir}/man1/mpic++.1*
%{_mandir}/man1/mpicc.1*
%{_mandir}/man1/mpicxx.1*
%{_mandir}/man1/mpif77.1*
%{_mandir}/man1/mpif90.1*
%{_mandir}/man1/mpifort.1*
%{_mandir}/man1/ompi-wrapper-compiler.1*
%{_mandir}/man1/opal_wrapper.1*
%{_mandir}/man3/MPI_*.3*
%{_mandir}/man3/MPIX_*.3*
%{_mandir}/man3/OMPI_*.3*

%files doc
%license LICENSE
%doc %{_docdir}/openmpi/html

%changelog
%autochangelog
