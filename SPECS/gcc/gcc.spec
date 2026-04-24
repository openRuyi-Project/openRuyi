# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define gcc_version 16
%define gcc_suffix 16

# Set to 1 to build the Ada compiler
%define build_ada 0
# Set to 1 to build the D compiler
%define build_d 0

%define quadmath_arch x86_64
%define libgccjit_sover 0
%define build_jit 0

Name:           gcc
URL:            http://gcc.gnu.org/
Version:        %{gcc_version}
Release:        %autorelease
Summary:        The system GNU C Compiler
License:        GPL-3.0-or-later
Source0:        cpp

BuildRequires:  gcc%{gcc_version}
BuildRequires:  gcc%{gcc_version}-c++
BuildRequires:  gcc%{gcc_version}-fortran
BuildRequires:  gcc%{gcc_version}-go
%if %{build_ada}
BuildRequires:  gcc%{gcc_version}-ada
%endif
%if %{build_d}
BuildRequires:  gcc%{gcc_version}-d
%endif
#!BuildIgnore: gcc%{gcc_version}-PIE

Requires:       cpp
Requires:       gcc%{gcc_version}

%description
The system GNU C Compiler.

%package     -n cpp
Summary:        The system GNU Preprocessor
License:        GPL-3.0-or-later
Requires:       cpp%{gcc_version}
# Only one of the symlink packages can be installed at the same time
Provides:       cpp = %{version}-%{release}
Conflicts:      cpp

%description -n cpp
The system GNU Preprocessor.

%package     -n gcc-c++
Summary:        The system GNU C++ Compiler
License:        GPL-3.0-or-later
Requires:       gcc%{gcc_version}-c++
Requires:       gcc = %{version}

%description -n gcc-c++
The system GNU C++ Compiler.

%package     -n libstdc++-devel
Summary:        The system GNU C++ development files
License:        GPL-3.0-only WITH GCC-exception-3.1
Requires:       libstdc++-devel-gcc%{gcc_version}

%description -n libstdc++-devel
The system GNU C++ development files.

%package     -n gcc-fortran
Summary:        The system GNU Fortran Compiler
License:        GPL-3.0-or-later
Requires:       gcc%{gcc_version}-fortran
Requires:       gcc = %{version}

%description -n gcc-fortran
The system GNU Fortran Compiler.

%package     -n gcc-objc
Summary:        The system GNU Objective C Compiler
License:        GPL-3.0-or-later
Requires:       gcc%{gcc_version}-objc
Requires:       gcc = %{version}

%description -n gcc-objc
The system GNU Objective C Compiler.

%package     -n gcc-obj-c++
Summary:        The system GNU Objective C++ Compiler
License:        GPL-3.0-or-later
Requires:       gcc%{gcc_version}-obj-c++
Requires:       gcc-objc = %{version}

%description -n gcc-obj-c++
The system GNU Objective C++ Compiler.

%package     -n gcc-ada
Summary:        The system GNU Ada Compiler
License:        GPL-3.0-or-later
Requires:       gcc%{gcc_version}-ada
Requires:       gcc = %{version}

%description -n gcc-ada
The system GNU Ada Compiler.

%package     -n gcc-go
Summary:        The system GNU Go Compiler
License:        GPL-3.0-or-later
Requires:       gcc%{gcc_version}-go
Requires:       gcc = %{version}
Requires(post): update-alternatives
Requires(postun): update-alternatives

%description -n gcc-go
The system GNU Go Compiler.

%package     -n gcc-d
Summary:        The system GNU D Compiler
License:        GPL-3.0-or-later
Requires:       gcc%{gcc_version}-d
Requires:       gcc = %{version}
Requires(post): update-alternatives
Requires(postun): update-alternatives

%description -n gcc-d
The system GNU D Compiler.

%package     -n libgccjit-devel
Summary:        Support for embedding GCC inside programs and libraries
License:        GPL-3.0-or-later
Requires:       libgccjit-devel-gcc%{gcc_version}

%description -n libgccjit-devel
Package contains header files and documentation for GCC JIT front-end.

%package     -n libquadmath-devel
Summary:        Development files for the quadprecision math library
License:        LGPL-2.1-only
Requires:       libquadmath-devel-gcc%{gcc_version}

%description -n libquadmath-devel
Development files for the quadprecision math library.

%package     -n libatomic
Summary:        The GNU Compiler Atomic Operations Runtime Library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Requires:       libatomic-gcc%{gcc_version}
# Only one of the symlink packages can be installed at the same time
Provides:       libatomic = %{version}-%{release}
Conflicts:      libatomic

%description -n libatomic
The system GNU Compiler Atomic Operations Runtime Library.

%package     -n libgomp
Summary:        The GNU Compiler OpenMP Runtime Library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Requires:       libgomp-gcc%{gcc_version}
# Only one of the symlink packages can be installed at the same time
Provides:       libgomp = %{version}-%{release}
Conflicts:      libgomp

%description -n libgomp
The system GNU Compiler OpenMP Runtime Library.

%package     -n libgfortran
Summary:        The GNU Fortran Compiler Runtime Library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Requires:       libgfortran-gcc%{gcc_version}
# Only one of the symlink packages can be installed at the same time
Provides:       libgfortran = %{version}-%{release}
Conflicts:      libgfortran

%description -n libgfortran
The system GNU Fortran Compiler Runtime Library.

%package     -n libobjc
Summary:        The GNU Objective C Compiler Runtime Library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Requires:       libobjc-gcc%{gcc_version}
# Only one of the symlink packages can be installed at the same time
Provides:       libobjc = %{version}-%{release}
Conflicts:      libobjc

%description -n libobjc
The system GNU Objective C Compiler Runtime Library.

%prep

%install
mkdir -p $RPM_BUILD_ROOT/lib
mkdir -p $RPM_BUILD_ROOT%{_prefix}/bin
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_infodir}
mkdir -p $RPM_BUILD_ROOT%{_prefix}/share/doc/packages/gcc-objc/
mkdir -p $RPM_BUILD_ROOT%{_prefix}/share/doc/packages/gcc-obj-c++/
# Link all the binaries
for program in \
        gcc gcov gcov-dump gcov-tool lto-dump \
        g++ \
        cpp \
        gfortran \
        gccgo \
%if %{build_ada}
        gnat gnatbind gnatchop gnatclean gnatkr \
        gnatlink gnatls gnatmake gnatname gnatprep \
%endif
%if %{build_d}
        gdc \
%endif
        gcc-ar gcc-nm gcc-ranlib \
    ; do
  ln -sf $program-%{gcc_suffix} $RPM_BUILD_ROOT%{_prefix}/bin/$program
done
# For go and gofmt use alternatives since they are shared with golang
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
ln -sf %{_sysconfdir}/alternatives/go %{buildroot}%{_bindir}/go
ln -sf %{_sysconfdir}/alternatives/gofmt %{buildroot}%{_bindir}/gofmt
# Link section 1 manpages
for man1 in \
        gcc gcov gcov-dump gcov-tool lto-dump \
        g++ \
        cpp \
        gfortran \
        gccgo \
%if %{build_d}
        gdc \
%endif
    ; do
  ln -sf $man1-%{gcc_suffix}.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/$man1.1.gz
done

# Provide the traditional /lib/cpp (as /usr/lib/cpp on usrmerged systems)
# that only handles C
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib
cp %{SOURCE0} $RPM_BUILD_ROOT%{_prefix}/lib/
chmod 755 $RPM_BUILD_ROOT%{_prefix}/lib/cpp
# Provide extra symlinks
ln -sf g++-%{gcc_suffix} $RPM_BUILD_ROOT%{_prefix}/bin/c++
ln -sf gcc-%{gcc_suffix} $RPM_BUILD_ROOT%{_prefix}/bin/cc
ln -sf g++-%{gcc_suffix}.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/c++.1.gz
ln -sf gcc-%{gcc_suffix}.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/cc.1.gz
# Install the LTO linker plugin so it is auto-loaded by BFD
mkdir -p $RPM_BUILD_ROOT%{_libdir}/bfd-plugins
ln -s `gcc-%{gcc_suffix} -print-file-name=liblto_plugin.so` $RPM_BUILD_ROOT%{_libdir}/bfd-plugins/liblto_plugin.so

%post -n gcc-go
# we don't want a BuildRequires on gccN-go but otherwise the install
# step of the build fails, so simply skip the script when gccN-go isn't there
if [ -f %{_bindir}/go-%{gcc_suffix} ] ; then
update-alternatives \
  --install %{_bindir}/go go %{_bindir}/go-%{gcc_suffix} 100 \
  --slave %{_bindir}/gofmt gofmt %{_bindir}/gofmt-%{gcc_suffix}
fi

%postun -n gcc-go
if [ $1 -eq 0 ] ; then
  update-alternatives --remove go %{_bindir}/go-%{gcc_suffix}
fi

%files -n gcc
%defattr(-,root,root)
%{_prefix}/bin/gcc
%{_prefix}/bin/cc
%{_prefix}/bin/gcov
%{_prefix}/bin/gcov-dump
%{_prefix}/bin/gcov-tool
%{_prefix}/bin/lto-dump
%{_prefix}/bin/gcc-ar
%{_prefix}/bin/gcc-nm
%{_prefix}/bin/gcc-ranlib
%dir %{_libdir}/bfd-plugins
%{_libdir}/bfd-plugins/liblto_plugin.so
%doc %{_mandir}/man1/gcc.1.gz
%doc %{_mandir}/man1/cc.1.gz
%doc %{_mandir}/man1/gcov.1.gz
%doc %{_mandir}/man1/gcov-dump.1.gz
%doc %{_mandir}/man1/gcov-tool.1.gz
%doc %{_mandir}/man1/lto-dump.1.gz

%files -n cpp
%defattr(-,root,root)
%{_prefix}/lib/cpp
%{_prefix}/bin/cpp
%doc %{_mandir}/man1/cpp.1.gz

%files -n gcc-c++
%defattr(-,root,root)
%{_prefix}/bin/g++
%{_prefix}/bin/c++
%doc %{_mandir}/man1/g++.1.gz
%doc %{_mandir}/man1/c++.1.gz

%files -n gcc-fortran
%defattr(-,root,root)
%{_prefix}/bin/gfortran
%doc %{_mandir}/man1/gfortran.1.gz

%files -n gcc-objc
%defattr(-,root,root)

%files -n gcc-obj-c++
%defattr(-,root,root)

%if %{build_ada}
%files -n gcc-ada
%defattr(-,root,root)
%{_prefix}/bin/gnat
%{_prefix}/bin/gnatbind
%{_prefix}/bin/gnatchop
%{_prefix}/bin/gnatclean
%{_prefix}/bin/gnatkr
%{_prefix}/bin/gnatlink
%{_prefix}/bin/gnatls
%{_prefix}/bin/gnatmake
%{_prefix}/bin/gnatname
%{_prefix}/bin/gnatprep
%endif

%files -n libstdc++-devel
%defattr(-,root,root)

%files -n gcc-go
%defattr(-,root,root)
%{_bindir}/gccgo
%{_bindir}/go
%{_bindir}/gofmt
%ghost %{_sysconfdir}/alternatives/go
%ghost %{_sysconfdir}/alternatives/gofmt
%doc %{_mandir}/man1/gccgo.1.gz

%if %{build_d}
%files -n gcc-d
%defattr(-,root,root)
%{_bindir}/gdc
%doc %{_mandir}/man1/gdc.1.gz
%endif

%if %{build_jit}
%files -n libgccjit-devel
%defattr(-,root,root)
%endif

%if %{gcc_version} >= 14
%ifarch %quadmath_arch
%files -n libquadmath-devel
%defattr(-,root,root)
%endif
%endif

%files -n libatomic
%defattr(-,root,root)

%files -n libgomp
%defattr(-,root,root)

%files -n libgfortran
%defattr(-,root,root)

%files -n libobjc
%defattr(-,root,root)

%changelog
%autochangelog
