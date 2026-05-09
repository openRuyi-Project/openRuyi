# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Bo YU <yubo@iscas.ac.cn>
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global major_version 2
%global minor_version 12
%global patch_version 2

Name:           hwloc
Summary:        Portable Hardware Locality - portable abstraction of hierarchical architectures
Version:        %{major_version}.%{minor_version}.%{patch_version}
Release:        %autorelease
License:        BSD-2-Clause
URL:            http://www.open-mpi.org/projects/hwloc/
VCS:            git:https://github.com/open-mpi/ompi
#!RemoteAsset:  sha256:ff7d309fdff7ceddfe15c1e79eaff25f3126a134f29f44d4e85571f187a6bab8
Source0:        https://download.open-mpi.org/release/hwloc/v%{major_version}.%{minor_version}/hwloc-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-plugins
BuildOption(conf):  --disable-silent-rules
BuildOption(conf):  --runstatedir=/run

# disabled features: plugins for GL,pci,libxml, X11 graphical interface, opencl support, rdma-core support, html doc
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(numa)
BuildRequires:  make
BuildRequires:  pkgconfig(libxml-2.0)

%description
The Portable Hardware Locality (hwloc) software package provides
a portable abstraction (across OS, versions, architectures, ...)
of the hierarchical topology of modern architectures, including
NUMA memory nodes,  shared caches, processor sockets, processor cores
and processing units (logical processors or "threads"). It also gathers
various system attributes such as cache and memory information. It primarily
aims at helping applications with gathering information about modern
computing hardware so as to exploit it accordingly and efficiently.

hwloc may display the topology in multiple convenient formats.
It also offers a powerful programming interface (C API) to gather information
about the hardware, bind processes, and much more.

%package        devel
Summary:        Headers and shared development libraries for hwloc
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers and shared object symbolic links for the hwloc.

%conf -a
# Remove rpaths
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%install -a
%ifnarch x86_64
# this shall not work under non-x86 arch
rm %{buildroot}%{_datadir}/hwloc/hwloc-dump-hwdata.service
%endif

%check -p
# Skip OBS unsupported sched_setaffinity() test.
sed -i 's/^{$/{return 77;/' tests/hwloc/glibc-sched.c

%files
%license COPYING
%doc AUTHORS NEWS README VERSION
%{_docdir}/hwloc/*.*
%{_datadir}/bash-completion/completions/*
%{_bindir}/hwloc*
# lstopo will not provide GUI mode, since X11 or
# wayland is not imported
%ifarch x86_64
%{_datadir}/hwloc/hwloc-dump-hwdata.service
%endif
%{_bindir}/lstopo
%{_bindir}/lstopo-no-graphics
%{_mandir}/man1/hwloc*
%{_mandir}/man1/lstopo-no-graphics.1.gz
%{_mandir}/man1/lstopo.1.gz
%{_mandir}/man7/hwloc*
%dir %{_datadir}/hwloc
%{_datadir}/hwloc/hwloc-ps.www/
%{_datadir}/hwloc/hwloc.dtd
%{_datadir}/hwloc/hwloc-valgrind.supp
%{_datadir}/hwloc/hwloc2.dtd
%{_datadir}/hwloc/hwloc2-diff.dtd
%{_libdir}/libhwloc*so.15*

%files devel
%{_libdir}/pkgconfig/hwloc.pc
%{_mandir}/man3/*
%dir %{_includedir}/hwloc
%{_includedir}/hwloc/*
%{_includedir}/hwloc.h
%{_libdir}/*.so

%changelog
%autochangelog
