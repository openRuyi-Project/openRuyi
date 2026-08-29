# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global prec_names prec_name[0]=single;prec_name[1]=double;prec_name[2]=long;prec_name[3]=quad

%ifarch x86_64
%global nprec 4
%else
%global nprec 3
%endif

Name:           fftw
Version:        3.3.11
Release:        %autorelease
Summary:        A Fast Fourier Transform library
License:        GPL-2.0-or-later AND MIT AND BSD-2-Clause
URL:            https://github.com/FFTW/fftw3
#!RemoteAsset:  sha256:5630c24cdeb33b131612f7eb4b1a9934234754f9f388ff8617458d0be6f239a1
Source0:        http://www.fftw.org/fftw-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake
%ifarch x86_64
BuildRequires:  libquadmath-devel
%endif

%description
FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.

%package        devel
Summary:        Headers, libraries and docs for the FFTW library
Requires:       pkgconfig
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for FFTW.

%conf -p
autoreconf -fiv

%conf
BASEFLAGS="--enable-shared --disable-dependency-tracking --enable-threads --enable-openmp --disable-static --disable-fortran"
# 0: single, 1: double, 2: long, 3: quad
%prec_names
prec_flags[0]=--enable-single
prec_flags[1]=--enable-double
prec_flags[2]=--enable-long-double
prec_flags[3]=--enable-quad-precision

%ifarch x86_64
for ((i=0; i<2; i++)) ; do prec_flags[i]+=" --enable-sse2 --enable-avx --enable-avx2"; done
%endif

for ((iprec=0; iprec<%{nprec}; iprec++)) ; do
    mkdir ${prec_name[iprec]}
    cd ${prec_name[iprec]}
    ln -s ../configure .
    %configure ${BASEFLAGS} ${prec_flags[iprec]}
    cd ..
done

%build
%prec_names
for ((iprec=0; iprec<%{nprec}; iprec++)) ; do
    cd ${prec_name[iprec]}
    %make_build
    cd ..
done

%install
%prec_names
for ((iprec=0; iprec<%{nprec}; iprec++)) ; do
    cd ${prec_name[iprec]}
    %make_install
    cd ..
done

# No check.
%check

%files
%{_mandir}/man1/fftw*.1*
%{_bindir}/fftw*-wisdom*
%doc AUTHORS ChangeLog NEWS README* TODO
%{_libdir}/libfftw3f.so.*
%{_libdir}/libfftw3f_threads.so.*
%{_libdir}/libfftw3f_omp.so.*
%{_libdir}/libfftw3.so.*
%{_libdir}/libfftw3_threads.so.*
%{_libdir}/libfftw3_omp.so.*
%{_libdir}/libfftw3l.so.*
%{_libdir}/libfftw3l_threads.so.*
%{_libdir}/libfftw3l_omp.so.*
%ifarch x86_64
%{_libdir}/libfftw3q.so.*
%{_libdir}/libfftw3q_threads.so.*
%{_libdir}/libfftw3q_omp.so.*
%endif

%files devel
%doc doc/FAQ/fftw-faq.html/
%doc %{_infodir}/fftw3.info*
%{_includedir}/fftw3*
%{_libdir}/cmake/fftw3/
%{_libdir}/pkgconfig/fftw3.pc
%{_libdir}/pkgconfig/fftw3f.pc
%{_libdir}/pkgconfig/fftw3l.pc
%ifarch x86_64
%{_libdir}/pkgconfig/fftw3q.pc
%endif
%{_libdir}/libfftw3*.so

%changelog
%autochangelog
