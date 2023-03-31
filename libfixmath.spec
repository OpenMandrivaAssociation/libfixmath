# static-only library...
%define debug_package %{nil}
%define devname %mklibname fixmath -d
# Static library should be usable with gcc as well,
# so let it contain object code rather than LLVM bitcode
%define _disable_lto 1

Name: libfixmath
Version: 2022.09.02
Release: 2
Source0: https://github.com/PetteriAimonen/libfixmath/archive/refs/heads/master.tar.gz
Patch0: https://salsa.debian.org/debian/libfixmath/-/raw/master/debian/patches/latomic.diff
Patch1: https://salsa.debian.org/debian/libfixmath/-/raw/master/debian/patches/tests-optional.diff
Summary: Fixed point math operations library
URL: https://github.com/PetteriAimonen/libfixmath
License: BSD
Group: System/Libraries
BuildRequires: cmake ninja
BuildRequires: atomic-devel

%description
Libfixmath implements Q16.16 format fixed point operations in C.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Provides: fixmath-devel = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Libfixmath implements Q16.16 format fixed point operations in C.

%prep
%autosetup -p1 -n %{name}-master
%cmake -G Ninja

%build
%ninja_build -C build

%install
mkdir -p %{buildroot}%{_libdir}
cp build/liblibfixmath.a %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}/libfixmath
cp libfixmath/*.h libfixmath/*.hpp %{buildroot}%{_includedir}/libfixmath

%files -n %{devname}
%{_includedir}/libfixmath
%{_libdir}/*.a
