Name: rquota
Version: 2.2.8
Release: 1

Summary: Quota utility for displaying remote NFS quotas
Group:   System Environment/Base
License: GPL
# we replace the redhat quota program
Conflicts: quota

BuildRoot: %{_tmppath}/%{name}-%{version}

Source0: %{name}-%{version}.tar.gz

%bcond_with lustre

%if 0%{?with_lustre}
BuildRequires: lustre
%endif

%description
Quota is a utility for displaying remote filesystem quota information.
This particular implentation does not report local filesystem quotas
as it is intended to run in a computing center where all user data
resides on shared NFS or Lustre servers.  In addition, quota only reports
filesystems listed in the quota.conf file to reduce latency in environments 
where there are many remote filesystems that are not configured with quotas.
Quotas are reported in human-readable units: 'K', 'M', and 'T' bytes.

%prep
%setup

%build
%configure \
	%{?with_lustre: --with-lustre} \
	--program-prefix=%{?_program_prefix:%{_program_prefix}}
make
make check

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root,0755)
%doc ChangeLog NEWS INSTALL README DISCLAIMER COPYING
%{_bindir}/quota
%{_bindir}/repquota
%{_mandir}/man1/quota.1*
%{_mandir}/man8/repquota.8*
%{_mandir}/man5/quota.conf.5*
%config(noreplace) %{_sysconfdir}/quota.conf
